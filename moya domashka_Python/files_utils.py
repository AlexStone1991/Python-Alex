import json
import csv
import yaml
from typing import List, Dict, Any

# Функции для работы с JSON

# 1 Функция read_json
def read_json(file_path: str, encoding: str = "utf-8") -> dict:
    """Читает данные из JSON-файла."""
    with open(file_path, 'r', encoding=encoding) as file:
        data = json.load(file)
    return data

# Функция write_json
def write_json(*data: dict, file_path: str, encoding: str = "utf-8") -> None:
    """Записывает данные в JSON-файл."""
    with open(file_path, 'w', encoding=encoding) as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# 3 Функция append_json
def append_json(*data: dict, file_path: str, encoding: str = "utf-8") -> None:
    """Добавляет данные в существующий JSON-файл."""
    existing_data = read_json(file_path, encoding)
    existing_data.extend(data)
    write_json(existing_data, file_path, encoding)

# Функции для работы с CSV
# 4 Функция read_csv

import csv

def read_csv(file_path: str, delimiter=';', encoding: str = 'utf-8-sig') -> list:
    """Читает данные из CSV-файла."""
    with open(file_path, 'r', encoding=encoding) as file:
        reader = csv.DictReader(file, delimiter=delimiter)
        data = [row for row in reader]
    return data

# 5 Функция write_csv
def write_csv(*data: dict, file_path: str, delimiter=';', encoding: str = 'utf-8-sig') -> None:
    """Записывает данные в CSV-файл."""
    with open(file_path, 'w', encoding=encoding, newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys(), delimiter=delimiter)
        writer.writeheader()
        writer.writerows(data)

# 6 Функция append_csv
def append_csv(*data: dict, file_path: str, delimiter=';', encoding: str = 'utf-8-sig') -> None:
    """Добавляет данные в существующий CSV-файл."""
    with open(file_path, 'a', encoding=encoding, newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys(), delimiter=delimiter)
        writer.writerows(data)


