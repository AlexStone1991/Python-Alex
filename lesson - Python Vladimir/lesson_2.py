"""
Lesson 2 
24.11.2024

- Правила наименования файлов, переменных
- Константы
- ID и переменные как ссылки
- Типы данных в пайтон
- Знакомство со строками
- Сочетания клавиш - @command:python.execInTerminal - можно назначить свой хоткей для старта кода
- f строки 
- r строки
- rf строки
- пример с путями файлов
- символ переноса строки
- len - длина строки
- Многострочкая rf строка

- отладочная строка
- input - ввод данных в консоль

- Типы ошибок. Синтаксические ошибки и логические ошибки

- аргументы принта
- art
- ascii_magic
"""

"""
1. Название переменной должно быть понятным на английском языке
2. Без пробелов. (можно использовать нижнее подчеркивание)
3. Не должно начинаться с цифры, но может содержать цифры
4. Не должно содержать спецсимволы
5. lower_snake_case - Мы пишем названия в нижнем регистре, разделяя слова нижним подчеркиванием
6. Как правило, это существительное, которое описывает переменную

is_ - Как правило для тех переменных которые являются булевыми
"""
# Константа. Изменяемая. Пишут в начале файла. Обычно какие-то настройк
FAVORITE_NUM = 8

a = 5
b = a
c = 5

print(a)
print(b)

b = 6

print(id(a))
print(id(b))
print(id(c))

print(a is b)  # Проверка на один и тот же объект
print(a == b)  # Проверка на одинаковое значение

# Типы данных в пайтон
"""
string - str() - строка
integer - int() - целое число
float - float() - число с плавающей точкой
boolean - bool() - булевое значение
list - list() - список
tuple - tuple() - кортеж
set - set() - множество
forzen set - frozenset() - замороженное множество
dict - dict() - словарь
"""

# Знакомство со строками

# Строки - неизменяемая последовательность символов, заключенная в одинарные или двойные кавычки
# Может быть заключена в тройные кавычки (многострочные строки)

name = "Геракл"
last_name = "Геркулесович"

poem = """
Шел Геракл через реку,
Видит в реке рак,
Рак Геракла хвать!

    Автор: Я
"""

print(poem)

full_name = name + " " + last_name
print(full_name)

# F-строки
full_name = f'{name} {last_name}'
print(full_name)

poem = f"""
Шел Геракл через реку,
Видит в реке рак,
Рак Геракла хвать!

    Автор: {name} {last_name}
"""

# Обратный слеш \ используется в Windows для путей
# Прямой слеш / используется в Unix-системах и URL

# Как мы можем записать кавычку в строке?
one = 'Я люблю "Наполеон"'
two = "Я люблю \"Наполеон\""

print(one, two)

file_path = r"С:\Users\nikolay\""
file_path2 = "С:\\Users\\nikolay\\"
print(file_path)
print(file_path2)

name = 'Nikolay'
home_dir = rf"C:\Users\{name}"
print(home_dir)

# - символ переноса строки \n
"""
Попробуйте вывести на экран 
"Символ переноса строки это \n"
"""

string = "Символ переноса строки это \\n"
print(string)

poem = f"Шел Геракл через реку,\nВидит в реке рак,\nРак Геракла хвать!\n\n\tАвтор: {name} {last_name}"

print(poem)

# len - встроенная функция, которая возвращает длину строки

print(f'Длина поэмы составила {len(poem)} символов')

# - отладочная строка
a = 5
b = 6

print(f'a = {a}')
print(f'b = {b}')
print(f'a + b = {a + b}')

# Отладочная строка это f'{переменная=}'
print(f'{a = }')
print(f'{b = }')
print(f'{a + b = }')
print(f'{len(poem) = }')

# input - ввод данных в консоль
# input всегда вернет строку
name = input('Введите ваше имя: ')
print(f'Привет, {name}!')




"""
Получите от пользователя имя, фамилию и возраст, соберите f стркоку
Привет <имя> <фамилия>, ваш возраст <возраст> лет
и выведите ее на экран
"""
first_name = input('Введите ваше имя: ')
last_name = input('Введите вашу фамилию: ')
age = input('Введите ваш возраст: ')

hello_message = f'Привет, {first_name} {last_name}, ваш возраст {age} лет'

print(hello_message)

# Типы ошибок. Синтаксические ошибки и логические ошибки

a = 2 
b = 0
# print(a / b) # ZeroDivisionError: division by zero


# - аргументы принта.
# sep - разделитель между аргументами принта (по умолчанию пробел)
# end - что выводить в конце принта (по умолчанию перенос строки)

print(a)
print(b)
print(a, b, sep = " || ")
print(a, b, sep = "\n")

print(a, end=" ")
print(b,  end=" Парапарапам!\n")

# Умножение строки на число - повторение строки N раз

print(f'{"-" * 25}{name} {last_name}{"-" * 25}')

# Способы выравнивания строк
# center - выравнивание по центру
# ljust - выравнивание по левому краю
# rjust - выравнивание по правому краю
# заполнитель - пробел по умолчанию, но может быть любой символ

language = 'Python'
print(language.center(8, "="))
print(language.ljust(20, "-"))
print(language.rjust(20, "*"))

# pip install art
from art import *
# Создаем классный текстовый баннер
tprint("Lesson 2")

# Можно выбрать разные стили шрифтов
tprint("Hello", font="block")
tprint("Hello", font="banner3-D")
tprint("Hello", font="doh")
tprint("Hello", font="isometric1")
tprint("Hello", font="letters")
tprint("Hello", font="alligator")
tprint("Hello", font="dotmatrix")
tprint("Hello", font="bubble")
tprint("Hello", font="digital")
tprint("Hello", font="binary")


# Получить случайное ASCII-искусство
print(art("random"))


# Создать рамку вокруг текста # small medium big
print(text2art("Coding", "small"))
print(text2art("Coding", "medium"))
print(text2art("Coding", "big"))


# Основные цвета ANSI
RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
YELLOW = '\033[93m'
RESET = '\033[0m'  # Сброс цвета

print(f"{RED}Это красный текст{RESET}")
print(f"{GREEN}Это зеленый текст{RESET}")
print(f"{BLUE}Это синий текст{RESET}")
print(f"{YELLOW}Это желтый текст{RESET}")

# pip install ascii_magic


from ascii_magic import AsciiArt
my_art = AsciiArt.from_image("./images/photo.jpg")
my_art.to_terminal()


