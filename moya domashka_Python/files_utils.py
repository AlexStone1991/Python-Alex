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

