import json
import csv
import yaml

# Функции для работы с JSON

# 1 Функция read_json
def read_json(file_path: str, encoding: str = "utf-8") -> dict:
    """Читает данные из JSON-файла."""
    with open(file_path, 'r', encoding=encoding) as file:
        data = json.load(file)
    return data

# 2 Функция write_json
def write_json(*data: dict, file_path: str, encoding: str = "utf-8") -> None:
    """Записывает данные в JSON-файл."""
    with open(file_path, 'w', encoding=encoding) as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# 3 Функция append_json
def append_json(*data: dict, file_path: str, encoding: str = "utf-8") -> None:
    """Добавляет данные в существующий JSON-файл."""
    existing_data = read_json(file_path, encoding)
    if isinstance(existing_data, list):
        existing_data.extend(data)
    else:
        existing_data = [existing_data] + list(data)
    write_json(*existing_data, file_path=file_path, encoding=encoding)

# Функции для работы с CSV
# 4 Функция read_csv
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

# Функции для работы с TXT
# 7 Функция read_txt
def read_txt(file_path: str, encoding: str = "utf-8") -> str:
    """Читает данные из текстового файла."""
    with open(file_path, 'r', encoding=encoding) as file:
        data = file.read()
    return data

# 8 Функция write_txt
def write_txt(*data: str, file_path: str, encoding: str = "utf-8") -> None:
    """Записывает данные в текстовый файл."""
    with open(file_path, 'w', encoding=encoding) as file:
        file.write(' '.join(data))

# 9 Функция append_txt
def append_txt(*data: str, file_path: str, encoding: str = "utf-8") -> None:
    """Добавляет данные в конец текстового файла."""
    with open(file_path, 'a', encoding=encoding) as file:
        file.write(' '.join(data))

# Функция для работы с YAML
# 10 Функция read_yaml
def read_yaml(file_path: str) -> dict:
    """Читает данные из YAML-файла."""
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data
