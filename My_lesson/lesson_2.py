"""
lesson 2 
"""

# Правила нейминга для переменных (файлов):

"""
1. Название переменной должно быть понятным на английском языке
2. Без пробелов. (можно использовать нижнее подчеркивание)
3. Не должно начинаться с цифры, но может содержать цифры
4. Не должно содержать спецсимволы
5. lower_snake_case - Мы пишем названия в нижнем регистре, разделяя слова нижним подчеркиванием
6. Как правило, это существительное, которое описывает переменную

7. is - как правило для тех переменных, которые возвращают True или False
"""

# константа. изменяемая. Пишут в начале файла. обычно какие то настроки
FAVORITE_NUM = 8
"""
a = 5
b = a
c = 5

print(a)
print(b)

b = 6

print(id(a))
print(id(b))
print(id(c))

print(a is b)  # Проверка на один и тот же обьект
print(a == b)  # проверка на одинаковые значения
"""

# Типы данных в пайтон

"""
string - str() - строка
integer - int() - целое число
float - float() - число с плавающей точкой
boolean - bool() - True или False
list - list() - список
tuple - tuple() - кортеж
set - set() - множество
forzen set - frozenset() - замороженное множество
dict - dict() - словарь
"""

# Знакомство со строками
#  Строки - это не изменяеммая последовательность символов, заключенная в одинарные или двойные кавчки
#  может быть заключена в тройные кавычки ( многострочные строки)

name = "Alex"
last_name = "Stone"

# Многострочные строки
poem = """
Шел геракл через реку,
Видит в реке рак,
Рак - чего ты так печальный
"""

# print(poem)
# full_name = name + " " + last_name = "Alex Stone"
full_name = name + last_name

# print(full_name)

# F - строки

full_name = f"{name} {last_name}"  # "Alex Stone" через букву f
# print(full_name)

# Обратный слеш \ используется в Windows для путей
#  Прямой слеш / используется в Unix системах и URL

one = 'Я "Наполеон"'
one2 = "Я 'Наполеон'"
two = "Я \"Наполеон\""

# print(one, one2, two)

file_path = r"C:\Users\nikolay\"" # r - raw string - необработанная строка 
file_path2 = "C:\\Users\\nikolay\\" # C:\Users\nikolay\
# print(file_path) # C:\Users\nikolay\"
# print(file_path2) # C:\Users\nikolay\

name = "Alex"
home_dir = rf"C:\Users\{name}" # rf - сырая строка
# print(home_dir) # C:\Users\Alex

# - символ переноса \n - перенос строки
# - символ табуляции \t - табуляция типо клавиша таб
name2 = "Alex \nStone"
# print(name2)

poem = f"Шел геракл через реку,\nВидит в реке рак,\nРак - чего ты так печальный\n\n\tТы ишак и не хочешь спать?"
print(poem)
# len - встроеная функция, которая возвращает длину строки
print(f"длина поэмыы: {len(poem)} символов")

a = 6
b = 5


# print(f"a = {a}")
# print(f"a + b = {a + b}")

# # откладочная строка это f{переменная=}
# print(f"{a = }")
# print(f"{b = }")
# print(f"{a + b = }")
# print(f"{len(poem) = }")

# input - ввод данных
# input всегда вернет строку!!!

# name = input("Введите ваше имя: ")
# famili = input("Введите вашу фамилию: ")
# vosrast = input("Введите ваш возраст: ")
# print(f"Привет, {name} {famili}!")
# print(f"Ваш возраст: {vosrast} лет!")

a = 2
b = 0
# print(a / b) # ZeroDivisionError: division by zero

# print(a)
# print(b)
# print(a, b , sep = " || ")
# print(a, b, sep = "\n")

# print(a, end=" ")
# print(b, end="Вауваувау!\n")
# умножение строки на число - повторение строки N раз

# print(f"{"-" * 25}{name} {famili}{"-" * 25}")
# способы выравнивания строк
# centre - по центру
# ljust - выравнивание влево край
# rjust - выравнивание вправо край
# заполнитель пробел по умолчанию, но может быть любой символ

language = "Python"
# print(language.center(20, "=")) # 20 символов включая и саму переменную если будет меньше то ничего не будет! 
# =======Python=======
# print(language.ljust(20, "-")) # Python--------------
# print(language.rjust(20, "*")) # **************Python

from art import *
# print(text2art("ALEXSTONE"))
# tprint("ALEXSTONE", font="block")

# print(text2art("ALEXSTONE", "small"))

# tprint("ALEXSTONE", font="banner3-D")
# tprint("ALEXSTONE", font="doh")
# tprint("ALEXSTONE", font="isometric1")
# tprint("ALEXSTONE", font="letters")
# tprint("ALEXSTONE", font="alligator")
# tprint("ALEXSTONE", font="dotmatrix")
# tprint("ALEXSTONE", font="bubble")
# tprint("ALEXSTONE", font="digital")
# tprint("ALEXSTONE", font="binary")
# TODO как окрашивать текст в терминале
# Основные цвета ANSI
RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
RESET = "\033[0m" # сброс цвета

print(f"{RED}RED{RESET}")
print(f"{GREEN}GREEN{RESET}")
print(f"{BLUE}BLUE{RESET}")
print(f"{YELLOW}YELLOW{RESET}")

# pip install asciimatics
# from ascii_magic import AsciiArt

# my_art = AsciiArt.from_image("imag.jpg", )
# my_art.to_terminal()
