# В данном задании вам необходимо реализовать три класса для работы с файлами: `TxtFileHandler`, `CSVFileHandler` и `JSONFileHandler`. Каждый класс должен обеспечивать чтение, запись и добавление данных в соответствующий формат файлов. При этом классы для CSV и JSON должны работать со списками словарей. Особое внимание уделите реализации метода добавления (APPEND) для JSON, чтобы корректно объединять новые данные с уже существующими в файле.

# 1. **TxtFileHandler**
#    - Методы:
#      - `read_file(filepath: str) -> str`: Читает данные из TXT файла. Если файл не найден, возвращает пустую строку.
#      - `write_file(filepath: str, *data: str) -> None`: Записывает переданные данные в файл, перезаписывая его, если он существует.
#      - `append_file(filepath: str, *data: str) -> None`: Добавляет данные в конец файла. Если файл не существует, он создается.
#    - **Обработка ошибок:**
#      - Все методы должны корректно обрабатывать исключения (например, `FileNotFoundError`, `PermissionError`) и использовать менеджер контекста `with`.

# 2. **CSVFileHandler**
#    - Методы:
#      - `read_file(filepath: str) -> list[dict]`: Читает CSV файл и возвращает список словарей, где ключи соответствуют заголовкам столбцов. Если файл не найден, возвращает пустой список.
#      - `write_file(filepath: str, data: list[dict]) -> None`: Записывает список словарей в CSV файл. Если файл существует, он перезаписывается. Заголовки CSV берутся из ключей первого словаря.
#      - `append_file(filepath: str, data: list[dict]) -> None`: Добавляет список словарей в конец CSV файла. Если файл не существует, он создается с заголовками, полученными из данных.
#    - **Обработка ошибок:**
#      - Обработка исключений, связанных с операциями ввода-вывода, и корректное закрытие файла через `with`.

# 3. **JSONFileHandler**
#    - Методы:
#      - `read_file(filepath: str) -> list[dict]`: Читает JSON файл и возвращает данные в виде списка словарей. Если файл не найден или пуст, возвращает пустой список.
#      - `write_file(filepath: str, data: list[dict]) -> None`: Записывает список словарей в JSON файл, перезаписывая его целиком.
#      - `append_file(filepath: str, data: list[dict]) -> None`: Реализует корректное добавление данных в JSON файл. Если файл существует и содержит список, новые данные должны дописываться к существующему списку, иначе файл перезаписывается новым списком.
#    - **Обработка ошибок:**
#      - Корректная работа с исключениями (например, `JSONDecodeError`, `FileNotFoundError`) и использование менеджера контекста `with` для безопасного чтения и записи.

import csv
import json

class TxtFileHandler:
    def read_file(self, filepath: str) -> str:
        """Читает данные из TXT файла."""
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            return ""
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")
            return ""

    def write_file(self, filepath: str, *data: str) -> None:
        """Записывает данные в TXT файл, перезаписывая его."""
        try:
            with open(filepath, 'w', encoding='utf-8') as file:
                file.writelines(data)
        except Exception as e:
            print(f"Ошибка при записи в файл: {e}")

    def append_file(self, filepath: str, *data: str) -> None:
        """Добавляет данные в конец TXT файла."""
        try:
            with open(filepath, 'a', encoding='utf-8') as file:
                file.writelines(data)
        except Exception as e:
            print(f"Ошибка при добавлении в файл: {e}")



# Примеры использования

# Работа с TXT файлами
txt_handler = TxtFileHandler()
txt_handler.write_file("example.txt", "Начало файла.\n")
txt_handler.append_file("example.txt", "Добавляем строку.\n")
content_txt = txt_handler.read_file("example.txt")
print("Содержимое TXT:\n", content_txt)

# Работа с CSV файлами
csv_handler = CSVFileHandler()
data_csv = [{'name': 'Alice', 'age': '30'}, {'name': 'Bob', 'age': '25'}]
csv_handler.write_file("example.csv", data_csv)
csv_handler.append_file("example.csv", [{'name': 'Charlie', 'age': '35'}])
content_csv = csv_handler.read_file("example.csv")
print("Содержимое CSV:\n", content_csv)

# Работа с JSON файлами
json_handler = JSONFileHandler()
data_json = [{'product': 'Laptop', 'price': 1500}, {'product': 'Phone', 'price': 800}]
json_handler.write_file("example.json", data_json)
json_handler.append_file("example.json", [{'product': 'Tablet', 'price': 600}])
content_json = json_handler.read_file("example.json")
print("Содержимое JSON:\n", content_json)
