# TODO ООП Ч2 Простое взаимодействие классов Практика урок 23

# -Класс TxtHandler - для работы с текстовыми документами
from typing import Tuple, List


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


if __name__ == "__main__":
    txt_handler = TxtHandler("lesson_23.txt")
    txt_handler.write("Привет", "мир")
    txt_handler.append("Запишем еще одну строку", "И еще одну")
    print(txt_handler.read())

