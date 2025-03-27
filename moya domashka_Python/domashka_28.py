import json
from typing import List, Dict, Any
from dataclasses import dataclass, field

class JsonReader:
    @staticmethod
    def read_file(filepath: str) -> List[Dict]:
        """
        Читает JSON-файл и возвращает данные в виде списка словарей.

        :param filepath: Путь к JSON-файлу.
        :return: Список словарей с данными из файла.
        """
        with open(filepath, 'r', encoding='utf-8') as file:
            return json.load(file)

@dataclass(order=True)
class City:
    name: str
    population: int
    subject: str = field(compare=False)
    district: str = field(compare=False)
    coords: str = field(compare=False)
    lat: float = field(default_factory=float)
    lon: float = field(default_factory=float)
    is_used: bool = field(default=False, compare=False)

    def __post_init__(self):
        """
        Выполняет валидацию полей после инициализации.
        """
        if not isinstance(self.name, str) or not self.name:
            raise ValueError("Название города должно быть непустой строкой.")
        if not isinstance(self.population, int) or self.population <= 0:
            raise ValueError("Население города должно быть положительным числом.")


class CitiesSerializer:
    def __init__(self, city_data: List[Dict[str, Any]]):
        """
        Инициализирует объект CitiesSerializer и создает список экземпляров City.

        :param city_data: Список словарей с данными городов.
        """
        self.cities = [City(**city) for city in city_data]

    def get_all_cities(self) -> List[City]:
        """
        Возвращает список экземпляров класса City.

        :return: Список объектов City.
        """
        return self.cities

def main():
    # Чтение данных из файла cities.json
    json_reader = JsonReader()
    city_data = json_reader.read_file('cities.json')

    # Создание списка городов с помощью CitiesSerializer
    serializer = CitiesSerializer(city_data)
    cities = serializer.get_all_cities()

    # Вывод списка экземпляров класса City
    for city in cities:
        print(city)

if __name__ == "__main__":
    main()