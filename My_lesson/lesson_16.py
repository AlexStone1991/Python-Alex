# TODO Функции. Ч3. Разбор ДЗ. Работа с файлами. Практика. Урок 16

txt_file = "lesson_16.txt"

# относительные пути
# ./ - текущая директория
# ../ - родительская директория
# ../../ - родительская директория родительской директории

# Абсолютные пути
# "C:\Users\ALEXSTONE\Desktop\домашка 2.jpg"

# открываем файл
# file = open(txt_file, "w",
# encoding="utf-8")

# # запишем в файл текст
# file.write("Первая строка" + "\n")
# file.write("Вторая строка" + "\n")

# file.close()

# ФЛаги
# r -  открывает файл только для чтения - падает с ошибкой если файла нет
# w - открывает файл для записи - создает файл если его нет
# a - открывает файл для добавления данных - создаст файл если его нет
# b - открыть файл в бинарном режиме

# Список функций для TXT
# open() - открывает файл и возвращает итератор
# read() - прочитать весь файл - возвращает строку с содержимым всего файла. Если файл большой, может занять много памяти
# readline() - прочитать одну строку - возвращает строку до символа переноса строки \n. При повторном вызове читает следующую строку
# readlines() - прочитать все строки и вернуть список строк - каждый элемент списка это отдельная строка с \n в конце
# write() - записать данные в файл - принимает строку, возвращает количество записанных символов. Не добавляет \n автоматически
# writelines() - записать список строк в файл - принимает список строк, не добавляет \n между строками автоматически. Нужно добавлять самостоятельно
# close() - закрывает файл и освобождает ресурсы. Важно всегда закрывать файлы после работы

file = open(txt_file, 'r', encoding="utf8") 
# <_io.TextIOWrapper name='lesson_16.txt' mode='r' encoding='utf8'>

# Интеративное чтение файла
# print(file)
# print(next(file))

# for line in file:
#     print(line)

# file.close() 
# print(file.readline().strip())
# print(file.readline().strip())
# print(file.readline().strip())

# lines = file.readlines()
# clear_lines = [line.strip() for line in lines]
# print(clear_lines)

# file.close()  # закрываем файл после работы

#  PRACTICE
"""
1. Функция чтения txt файла read_txt(file_path: str, encoding: str = "utf-8") -> list[str]
2. Функция записи txt файла write_txt(file_path: str, data: list[str], encoding: str = "utf-8") -> None
3. Функция добавления txt файла append_txt(file_path: str, data: list[str], encoding: str = "utf-8") -> None
"""
def read_txt(file_path: str, encoding: str = "utf-8") -> list[str]
    """
    Функции для текстового документа
    :param :
    :return :
    :raise :

    """
    file = open(file_path, 'r', encoding="utf-8")
    lines = file.readlines()
    clear_lines = [line.strip() for line in lines]
    file.close()
    return clear_lines

def write_txt(file_path: str, data: list[str], encoding: str = "utf-8") -> None:
    """
    Функции для текстового документа
    :param :
    :return :
    :raise :

    """
    file = open(file_path, 'w', encoding=encoding)
    file.writelines(data)
    file.close()


def append_txt(file_path: str, data: list[str], encoding: str = "utf-8") -> None:
    """
    Функции для текстового документа
    :param :
    :return :
    :raise :

    """
    file = open(file_path, 'a', encoding=encoding)
    file.writelines(data)
    file.close()
