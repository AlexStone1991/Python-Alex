from abc import ABC, abstractmethod
import json
import csv

class AbstractFile(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass

    @abstractmethod
    def append(self, data):
        pass

class JsonFile(AbstractFile):
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            return json.load(file)

    def write(self, data):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def append(self, data):
        try:
            existing_data = self.read()
        except FileNotFoundError:
            existing_data = []

        if isinstance(existing_data, list):
            existing_data.append(data)
        else:
            raise ValueError("Existing data is not a list")

        self.write(existing_data)

class TxtFile(AbstractFile):
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            return file.read()

    def write(self, data):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            file.write(data)

    def append(self, data):
        with open(self.file_path, 'a', encoding='utf-8') as file:
            file.write(data)

class CsvFile(AbstractFile):
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        with open(self.file_path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            return list(reader)

    def write(self, data):
        with open(self.file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(data)

    def append(self, data):
        with open(self.file_path, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(data)
