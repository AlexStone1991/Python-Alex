# TODO Функции. Ч4.Работа с файлами.TXT CSV JSON YAML. Урок 17.

def read_txt(file_path: str, encoding: str = "utf-8") -> list[str]:
    """
    Функция для текстового документа.
    :param  :
    :return :
    :raise :
    """
    file = open(file_path, "r", encoding=encoding)
    lines = file.readlines()
    clear_lines = [line.strip() for line in lines]
    file.close()
    return clear_lines


def write_txt(file_path: str, data: list[str], encoding: str = "utf-8") -> None:
    """
    Функция для текстового документа.
    :param  :
    :return :
    :raise :
    """
    file = open(file_path, "w", encoding=encoding)
    file.writelines(data)
    file.close()



def append_txt(file_path: str, data: list[str], encoding: str = "utf-8") -> None:
    """
    Функция для текстового документа.
    :param  :
    :return :
    :raise :
    """
    file = open(file_path, "a", encoding=encoding)
    file.writelines(data)
    file.close()

with open("lesson_17.txt", "w", encoding="utf-8") as file:
    file.write("Первая строка\n")
    file.write("Вторая строка\n")