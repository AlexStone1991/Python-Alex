from dataclasses import dataclass, field
from typing import List, Dict, Any
import json
import random

JSON_DATA = "cities.json"

class JsonHandler:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def read(self):
        """
        Читает данные из JSON-файла. Ensure_ascii=False - сохраняет русские символы
        Encoding='utf-8' - кодировка файла
        """
        with open(self.file_path, 'r', encoding='utf-8') as file:
            return json.load(file)

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
        """
        Выполняет валидацию полей после инициализации.
        """
        if not isinstance(self.name, str) or not self.name:
            raise ValueError("Название города должно быть непустой строкой.")
        if not isinstance(self.population, int) or self.population <= 0:
            raise ValueError("Население города должно быть положительным числом.")
        
class CitiesSerializer:
    def __init__(self, city_data: List[dict]):
        """
        Инициализирует объект CitiesSerializer и создает список экземпляров City.

        :param city_data: Список словарей с данными городов.
        """
        self.cities_data = city_data
        self.cities = self.__create_cities()

    def __deserialize_city(self, city_dict: dict) -> City:
        instance = City(
            name=city_dict['name'],
            population=city_dict['population'],
            subject=city_dict['district'],
            district=city_dict['district'],
            latitude=city_dict["coords"]['lat'],
            longitude=city_dict["coords"]['lon']
        )
        return instance
    def __create_cities(self) -> list:
        return [self.__deserialize_city(city_data) for city_data in self.cities_data]
    def get_all_cities(self) -> list[City]:
        return self.cities
    


class CityGame:
    def __init__(self, cities_serializer: CitiesSerializer):
        """
        Инициализирует игру на основе списка городов.

        :param cities_serializer: Сериализатор, содержащий список объектов City.
        """
        self.cities = cities_serializer.get_all_cities()
        self.used_cities = set()
        self.last_city = None

    def human_turn(self, city_input: str) -> bool:
        """
        Обрабатывает ход человека: проверяет корректность введенного названия и обновляет состояние.

        :param city_input: Название города, введенное игроком.
        :return: True, если ход корректен, иначе False.
        """
        city_input = city_input.strip().capitalize()

        if not city_input:
            print("Название города не может быть пустым. Попробуйте еще раз.")
            return False

        if self.last_city and not city_input.startswith(self.last_city[-1].upper()):
            print(f"Город должен начинаться на букву '{self.last_city[-1].upper()}'. Попробуйте еще раз.")
            return False

        city = next((c for c in self.cities if c.name == city_input), None)
        if not city:
            print("Такого города нет в базе. Попробуйте еще раз.")
            return False

        if city.is_used:
            print("Этот город уже был использован. Попробуйте еще раз.")
            return False

        city.is_used = True
        self.used_cities.add(city.name)
        self.last_city = city.name
        return True

    def computer_turn(self) -> str:
        """
        Находит подходящий город для хода компьютера и обновляет состояние игры.

        :return: Название города, выбранного компьютером.
        """
        if not self.last_city:
            # Если это первый ход, компьютер выбирает случайный город
            available_cities = [city for city in self.cities if not city.is_used]
        else:
            # Иначе, компьютер выбирает город, начинающийся на последнюю букву предыдущего города
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
        """
        Проверяет наличие возможных ходов и определяет завершение игры.

        :return: True, если игра завершена, иначе False.
        """
        if not self.last_city:
            return False

        last_char = self.last_city[-1].upper()
        available_cities = [city for city in self.cities if not city.is_used and city.name.startswith(last_char)]
        return len(available_cities) == 0

    def save_game_state(self) -> None:
        """
        Сохраняет текущее состояние игры в JSON-файл для возможности восстановления.
        """
        game_state = {
            "used_cities": list(self.used_cities),
            "last_city": self.last_city
        }
        with open("game_state.json", "w", encoding="utf-8") as file:
            json.dump(game_state, file, ensure_ascii=False, indent=4)

class GameManager:
    def __init__(self, json_file: JsonHandler, cities_serializer: CitiesSerializer, city_game: CityGame):
        """
        Инициализирует менеджер игры.

        :param json_file: Обработчик JSON-файла.
        :param cities_serializer: Сериализатор, содержащий список объектов City.
        :param city_game: Логика игры.
        """
        self.json_file = json_file
        self.cities_serializer = cities_serializer
        self.city_game = city_game

    def __call__(self):
        """
        Запускает игру, организуя последовательность ходов до завершения игры.
        """
        self.run_game()

    def run_game(self):
        """
        Координирует взаимодействие между компонентами и обеспечивает логическую последовательность ходов.
        """
        print("Добро пожаловать в игру 'Города'!")
        print("Компьютер делает первый ход...")

        while True:
            computer_city = self.city_game.computer_turn()
            if not computer_city:
                print("Компьютер не может сделать ход. Вы выиграли!")
                break
            print(f"Компьютер назвал город: {computer_city}")

            if self.city_game.check_game_over():
                print("Игра завершена. Вы проиграли!")
                break

            while True:
                city_input = input("Ваш ход (введите название города или 'стоп' для завершения игры): ")
                if city_input.lower() == "стоп":
                    print("Игра остановлена. Спасибо за участие!")
                    return
                if self.city_game.human_turn(city_input):
                    break

            if self.city_game.check_game_over():
                print("Игра завершена. Компьютер не может сделать ход. Вы выиграли!")
                break

if __name__ == "__main__":
    json_file = JsonHandler("cities.json")
    cities_data = json_file.read()
    cities_serializer = CitiesSerializer(cities_data)
    city_game = CityGame(cities_serializer)
    game_manager = GameManager(json_file, cities_serializer, city_game)
    game_manager()