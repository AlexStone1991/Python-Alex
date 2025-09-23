import tkinter as tk
from tkinter import messagebox
import random
import json
from dataclasses import dataclass, field
from typing import List

# Класс City представляет город с его основными характеристиками.
@dataclass
class City:
    name: str = field(compare=False)
    population: int
    subject: str = field(compare=False)
    district: str = field(compare=False)
    latitude: float = field(compare=False)
    longitude: float = field(compare=False)
    is_used: bool = field(default=False, compare=False, init=False)

    def __post_init__(self):
        # Проверка корректности данных после инициализации.
        if not isinstance(self.name, str) or not self.name:
            raise ValueError("Название города должно быть непустой строкой.")
        if not isinstance(self.population, int) or self.population <= 0:
            raise ValueError("Население города должно быть положительным числом.")

# Класс CitiesSerializer отвечает за преобразование данных из JSON в список объектов City.
class CitiesSerializer:
    def __init__(self, city_data: List[dict]):
        self.cities_data = city_data
        self.cities = self.__create_cities()

    def __deserialize_city(self, city_dict: dict) -> City:
        # Преобразование словаря в объект City. Решил сделать сразу через return
        # у Владимира было через переменную!
        return City(
            name=city_dict['name'],
            population=city_dict['population'],
            subject=city_dict['district'],
            district=city_dict['district'],
            latitude=city_dict["coords"]['lat'],
            longitude=city_dict["coords"]['lon']
        )

    def __create_cities(self) -> list:
        # Создание списка объектов City из данных.
        return [self.__deserialize_city(city_data) for city_data in self.cities_data]

    def get_all_cities(self) -> list:
        # Возвращает список всех городов.
        return self.cities

# Класс JsonHandler отвечает за чтение данных из JSON-файла.
class JsonHandler:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def read(self):
        # Чтение данных из JSON-файла.
        with open(self.file_path, 'r', encoding='utf-8') as file:
            return json.load(file)

# Класс CityGame управляет логикой игры "Города".
class CityGame:
    def __init__(self, cities_serializer: CitiesSerializer):
        self.cities = cities_serializer.get_all_cities()
        self.used_cities = set()
        self.last_city = None

    def human_turn(self, city_input: str) -> bool:
        # Обработка хода игрока.
        city_input = city_input.strip().capitalize()

        if not city_input:
            messagebox.showinfo("Ошибка", "Название города не может быть пустым.")
            return False

        if self.last_city and not city_input.startswith(self.last_city[-1].upper()):
            messagebox.showinfo("Ошибка", f"Город должен начинаться на букву '{self.last_city[-1].upper()}'.")
            return False

        city = next((c for c in self.cities if c.name == city_input), None)
        if not city:
            messagebox.showinfo("Ошибка", "Такого города нет в базе.")
            return False

        if city.is_used:
            messagebox.showinfo("Ошибка", "Этот город уже был использован.")
            return False

        city.is_used = True
        self.used_cities.add(city.name)
        self.last_city = city.name
        return True

    def computer_turn(self) -> str:
        # Ход компьютера.
        if not self.last_city:
            available_cities = [city for city in self.cities if not city.is_used]
        else:
            last_char = self.last_city[-1].upper()
            available_cities = [city for city in self.cities if not city.is_used and city.name.startswith(last_char)]

        if not available_cities:
            return ""

        chosen_city = random.choice(available_cities)
        chosen_city.is_used = True
        self.used_cities.add(chosen_city.name)
        self.last_city = chosen_city.name
        return chosen_city.name

    def check_game_over(self) -> bool:
        # Проверка завершения игры.
        if not self.last_city:
            return False

        last_char = self.last_city[-1].upper()
        available_cities = [city for city in self.cities if not city.is_used and city.name.startswith(last_char)]
        return len(available_cities) == 0

# Класс GameManager управляет интерфейсом и взаимодействием между компонентами игры.
class GameManager:
    def __init__(self, json_file: JsonHandler, cities_serializer: CitiesSerializer, city_game: CityGame):
        self.json_file = json_file
        self.cities_serializer = cities_serializer
        self.city_game = city_game

    def run_game(self):
        # Запуск игры и создание интерфейса.
        root = tk.Tk()
        root.title("Игра в Города")
        root.geometry("400x200")  # Увеличение размера окна

        self.info_label = tk.Label(root, text="Добро пожаловать в игру 'Города'!")
        self.info_label.pack()

        self.city_entry = tk.Entry(root)
        self.city_entry.pack()

        self.submit_button = tk.Button(root, text="Ввести город", command=self.process_turn)
        self.submit_button.pack()

        self.stop_button = tk.Button(root, text="Стоп", command=root.destroy)
        self.stop_button.pack()

        self.computer_turn()

        root.mainloop()

    def process_turn(self):
        # Обработка хода игрока и обновление интерфейса.
        city_input = self.city_entry.get()
        if city_input.lower() == "стоп":
            messagebox.showinfo("Информация", "Игра остановлена. Спасибо за участие!")
            return

        if self.city_game.human_turn(city_input):
            self.info_label.config(text=f"Вы назвали город: {city_input}")
            self.city_entry.delete(0, tk.END)  # Очистка поля ввода
            if self.city_game.check_game_over():
                messagebox.showinfo("Информация", "Игра завершена. Компьютер не может сделать ход. Вы выиграли!")
                return
            self.computer_turn()

    def computer_turn(self):
        # Ход компьютера и обновление интерфейса.
        computer_city = self.city_game.computer_turn()
        if not computer_city:
            messagebox.showinfo("Информация", "Компьютер не может сделать ход. Вы выиграли!")
            return
        self.info_label.config(text=f"Компьютер назвал город: {computer_city}")
        if self.city_game.check_game_over():
            messagebox.showinfo("Информация", "Игра завершена. Вы проиграли!")
            return

if __name__ == "__main__":
    json_file = JsonHandler("cities.json")
    cities_data = json_file.read()
    cities_serializer = CitiesSerializer(cities_data)
    city_game = CityGame(cities_serializer)
    game_manager = GameManager(json_file, cities_serializer, city_game)
    game_manager.run_game()
