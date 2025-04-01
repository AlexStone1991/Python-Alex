from dataclasses import dataclass, field
from typing import List, Dict, Any
import json

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
    
json_handler = JsonHandler(JSON_DATA)
city_data = json_handler.read()
cities_serializer = CitiesSerializer(city_data)
cities = cities_serializer.get_all_cities()
print(cities[0])