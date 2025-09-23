# TODO ООП Ч2 Простое взаимодействие классов Практика урок 23

# -Класс TxtHandler - для работы с текстовыми документами
from typing import Tuple, List
import requests
import tkinter as tk

SETTINGS = {
    "appid": "23496c2a58b99648af590ee8a29c5348",
    "units": "metric",
    "lang": "ru",
}


class Weather:
    """
    Класс для получения погоды из API OpenWeatherMap.
    """

    requsts_url = "https://api.openweathermap.org/data/2.5/weather?q={city}&appid={appid}&units={units}&lang={lang}"

    def __init__(self, appid: str, units: str, lang: str):
        self.appid = appid
        self.units = units
        self.lang = lang
        self.url: str = ""

    def get_url(self, city: str) -> str:
        """
        Формирует url для запроса к API OpenWeatherMap.
        :param city: Название города.
        :return: Сформированный url.
        """
        self.url = self.requsts_url.format(
            city=city, appid=self.appid, units=self.units, lang=self.lang
        )
        return self.url

    def format_response(self, response: dict) -> str:
        """
        Форматирует ответ API OpenWeatherMap.
        :param response: Ответ API в формате словаря.
        :return: Отформатированная строка с информацией о погоде.
        """
        temp = response["main"]["temp"]
        feels_like = response["main"]["feels_like"]
        return f"Температура: {temp}°C, ощущается как {feels_like}°C"

    def get_weather(self, city: str) -> str:
        """
        Получает и форматирует погоду для заданного города.
        :param city: Название города.
        :return: Информация о погоде.
        """
        url = self.get_url(city)
        try:
            response = requests.get(url)
            data = response.json()
            return self.format_response(data)
        except requests.exceptions.RequestException as e:
            return f"Ошибка при получении данных для города {city} - {str(e)}"

    def __call__(self, city: str) -> str:
        """
        Делает объект вызываемым.
        :param city: Название города.
        :return: Информация о погоде.
        """
        return f"Город: {city.capitalize()}, {self.get_weather(city)}"

class TxtHandler:
    # класс для работы с текстовыми документами
    # Methods:
    # - read()->List[str]: Возвращает список строк из файла
    #     - write(*data: Tuple[str, ...])->None: записывает данные в файл
    #     - append(*data: Tuple[str, ...])->None: добавляет данные в файл
    # Exceptions:
    #     - FileNotFoundError: если файл не найден
    #     - PermissionError: если нет прав на запись в файл

    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def read(self) -> list[str]:
        """
        Читает данные из файла и возвращает список строк.
        :return: Список строк из файла.
        :raise FileNotFoundError: если файл не найден.
        :raise PermissionError: если нет прав на чтение файла.
        """
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                row_data = file.readlines()
                return [row.strip() for row in row_data]
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл {self.file_path} не найден")
        except PermissionError:
            raise PermissionError(f"Нет прав на чтение файла {self.file_path}")

    def write(self, *data: str) -> None:
        """
        Записывает данные в файл.
        :param data: Данные для записи.
        :raise PermissionError: если нет прав на запись в файл.
        """
        prepared_data = [line + "\n" for line in data]
        try:
            with open(self.file_path, "w", encoding="utf-8") as file:
                file.writelines(prepared_data)
        except PermissionError:
            raise PermissionError(f"Нет прав на запись в файл {self.file_path}")

    def append(self, *data: str) -> None:
        """
        Добавляет данные в конец файла.
        :param data: Данные для записи.
        :raise PermissionError: если нет прав на запись в файл.
        """
        prepared_data = [line + "\n" for line in data]
        try:
            with open(self.file_path, "a", encoding="utf-8") as file:
                file.writelines(prepared_data)
        except PermissionError:
            raise PermissionError(f"Нет прав на запись в файл {self.file_path}")

class WeatherGUI:
    """
    Класс для создания простого графического интерфейса.
    При нажатии на кнопку вводится название города, выводится информация о погоде,
    а данные логируются в текстовый файл.
    """
    def __init__(self, weather: Weather, txt_handler: TxtHandler) -> None:
        self.weather = weather
        self.txt_handler = txt_handler
        self.root = tk.Tk()
        self.root.title("Погодное приложение")

        self.city_label = tk.Label(self.root, text="Введите название города:")
        self.city_label.pack(pady=5)

        self.city_entry = tk.Entry(self.root, width=40)
        self.city_entry.pack(pady=5)

        self.fetch_button = tk.Button(self.root, text="Получить погоду", command=self.get_weather)
        self.fetch_button.pack(pady=5)

        self.output_text = tk.Text(self.root, height=10, width=70)
        self.output_text.pack(pady=5)

    def get_weather(self) -> None:
        """
        Обрабатывает нажатие на кнопку, получает введённый город, формирует запрос,
        логирует и отображает результат в текстовом поле.
        """
        city = self.city_entry.get().strip()
        if city.lower() == "exit":
            self.root.quit()
            return
        weather_info = self.weather(city)
        self.txt_handler.append(weather_info)
        self.output_text.insert(tk.END, f"{weather_info}\n")
        self.city_entry.delete(0, tk.END)

    def run(self) -> None:
        """
        Запускает главный цикл графического интерфейса.
        """
        self.root.mainloop()


class WeatherFacade:
    """
    Класс фасад для работы с погодой и логированием данных о погоде в текстовый файл.
    """
    def __init__(self) -> None:
        self.weather = Weather(**SETTINGS)
        self.txt_handler = TxtHandler("weather.txt")
        self.gui = WeatherGUI(self.weather, self.txt_handler)

    def __call__(self) -> None:
        """
        Запускает логику программы
        :return: None
        """
        while True:
            self.gui.run()


if __name__ == "__main__":
    weather_facade = WeatherFacade()
    weather_facade()