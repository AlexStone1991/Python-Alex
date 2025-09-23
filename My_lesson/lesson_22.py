# TODO ООП. Ч1. Атрибуты и методы. Класс и экземпляр. Практика. Урок 22.

#  - class
# - нейминг классов UpperCamelCase
# - __init__ - иницилизатор
#  - self - ссылка на экземпляр класса
# - __new__ - как скрытая часть конструктора
# - методы работающие с self - методы экземпляра
# - документация класса и методов
import requests
from typing import Generator
# класс обЪявления
# class AdPost:
#     promote_rate: float = 0.1
#     def __init__(self, title: str, text: str, price: int):
#         self.title = title
#         self.text = text
#         self.price = price
#         # self.promote_rate: float = 0.5
    
#     def __str__(self) -> str:
#         return f"Класс: {self.__class__.__name__},Заголовок: {self.title}, Текст: {self.text[:20]}, цена: {self.price}"
    
#     def calculate_promote_cost(self, day: int) -> int:
#         promote_cost = int(self.price * (self.promote_rate / 100) * day)
#         return promote_cost

#     @staticmethod
#     def get_peak_hours() -> tuple:
#         # метод возращающий часы пик для размещения рекламы
#         # return кортеж с часами пик
#         return 13, 14, 15
    
#     @classmethod
#     def get_promote_rate(cls) -> float:
#         # метод возвращабзий теккущий процент рекламы
#         # ретурн процент рекламы
#         return cls.promote_rate
    
#     @classmethod
#     def set_promote_rate(cls, new_rate: float) -> None:
#         # метод устанавливающий новый процент рекламы
#         # принимает новый процент рекламы и устанавливает его в класс
#         cls.promote_rate = new_rate

# ap1 = AdPost("Sony playstation 5. Муха не сидела!", "Новая, красивая, блестящая...!", 20000)
# ap2 = AdPost("Видеокарта RTX 3090", "Как новая", 60000)

# AdPost.promote_rate = 1

# print(ap1)
# print(ap2)
# print(ap1.calculate_promote_cost(3),"рублей")
# print(ap2.calculate_promote_cost(3),"рублей")

# print(AdPost.get_peak_hours())
# print(AdPost.get_promote_rate())
# AdPost.set_promote_rate(5)
# print(AdPost.get_promote_rate())

# # // https://api.openweathermap.org/data/2.5/weather?q=Усть-Каменогорск&appid=23496c2a58b99648af590ee8a29c5348&units=metric&lang=ru

# cities_list = ["Бангкок", "Сеул", "Токио", "Усть-Каменогорск", "Барнаул", "Москва"]

# # pip install requests


# def get_weather(city: str) -> str:
#     # Базовый url API
#     url = "https://api.openweathermap.org/data/2.5/weather"
    
#     # Параметры GET запроса
#     params = {
#         "q": city,
#         "appid": "23496c2a58b99648af590ee8a29c5348",
#         "units": "metric",
#         "lang": "ru",
#     }

#     # Сам запрос. 
#     try:
#         response = requests.get(url, params=params)
#         data = response.json()
#         temp = data["main"]["temp"]
#         feels_like = data["main"]["feels_like"]

#     except requests.exceptions.RequestException as e:
#         return f"Ошибка при получении данных для города {city} - {str(e)}"
    
#     return f"Город: {city}, Температура: {temp}°C, ощущается как {feels_like}°C"

# # for city in cities_list:
# #     print(get_weather(city))


# # Это же, на генераторе
# def get_weather_gen(cities: list[str]) -> Generator[str]:
#     for city in cities:
#         yield get_weather(city)

# for weather in get_weather_gen(cities_list):
#     print(weather)

requsts_url = "https://api.openweathermap.org/data/2.5/weather?q={city}&appid={appid}&units={units}&lang={lang}"

class Weather:
    requsts_url = "https://api.openweathermap.org/data/2.5/weather?q={city}&appid={appid}&units={units}&lang={lang}"

    def __init__(self, appid: str, units: str, lang: str):
        self.appid = appid
        self.units = units
        self.lang = lang
        self.url: str = ""

    def get_url(self, city: str) -> str:
        self.url = self.requsts_url.format(city=city, appid=self.appid, units=self.units, lang=self.lang)
        return self.url
    
    def format_response(self, response: dict) -> str:
        temp = response["main"]["temp"]
        feels_like = response["main"]["feels_like"]
        return f"Город: {response['name']}, Температура: {temp}°C, ощущается как {feels_like}°C"
    
    def get_weather(self, city: str) -> str:
        url = self.get_url(city)
        try:
            response = requests.get(url)
            data = response.json()
            return self.format_response(data)
        except requests.exceptions.RequestException as e:
            return f"Ошибка при получении данных для города {city} - {str(e)}"
        
    def __call__(self, city: str) -> str:
        return f"Город: {city}, {self.get_weather(city)}"
    
# Тест
if __name__ == "__main__":
    weather = Weather(appid="23496c2a58b99648af590ee8a29c5348", units="metric", lang="ru")
    # Это без __call__
    moscow = weather.get_weather("Москва")
    # __call__ сделал мой обьект вызываемым
    sanct_petersburg = weather("Санкт-петербург")

    print(moscow)
    print(sanct_petersburg)
