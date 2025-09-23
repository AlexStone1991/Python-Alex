# TODO Python. print. input. Математика. Округление, Math. Random. Урок 3

# a = input("Введите число: ")
# b = input("Введите число: ")

# a = int(a)
# b = int(b)

# c = int(input("Введите число: "))

# print(f"Сумма: {a + b}")
# print(f"Разность: {a - b}")
# print(f"Произведение: {a * b}")
# print(f"{(a+b)*c}")

# Базовые математические операции
# Сложение a + b
# Вычитание a - b
# Умножение a * b
# Деление a / b
# Целочисленное деление a // b
# Остаток от деления a % b
# Возведение в степень a ** b

"""
1. Введите количество гостей
2. Введите сколько человек помещается в один автобус
3. Вывести сколько автобусов нужно заказать (используя целочисленное деление)
4. Вывести сколько человек останется (используя остаток от деления)
"""

# gosty = int(input("Введите количество гостей: "))
# avtobus = int(input("Введите сколько человек помещается в один автобус: "))

# autobuses = avtobus // gosty
# print(f"Нужно заказать {autobuses} автобусов")

# ostalos = avtobus % gosty
# print(f"Останется {ostalos} человек")

# import random # при обращении к модулю random мы получаем обьект модуля и все функции модуля. вызов random.chose
from random import randint, random, choice, shuffle, sample
# импортируем конкретные фунекции из мдуля random. вызов randin

# randint(a, b) - случайное целое число от а до b включительно
# randomm() - случайное число от 0 до 1
# choice(seq) - случайный элемент из последовательности
# shuffle(seq) - перемешивает последовательность
# sample(population, k) - случайная выборка элементов без повторений
# word = "Hello"

# word_listt = list(word)
# shuffle(word_listt)
# print(word_listt)


# print(randint(1, 10))
# print(random())
# print(choice(word))

# print(sample(word, 3))

"""
Попробуем сделать перемешивание строки через sample
1. Получить у пользователя строку
2. Получить длину строки через len
3. Создать переменную и положить туда результат вызова sample с параметрами sample(строка, длина строки)
4. Применить join к переменной и вывести на экран  " ".join(переменная)
"""

# stroka = input("Введите строку: ")
# print(f"длинна строки: {len(stroka)}")
# resh = sample(stroka, len(stroka))
# print(" ".join(resh))

from decimal import Decimal

# print(Decimal(0.1) + Decimal(0.2))

# функция приведения bool
# bool(value)
"""
print(f"{bool(0)=}")
print(f"{bool(1)=}")
print(f"{bool(-1)=}")

# дробные числа

print(f"{bool(0.0)=}")
print(f"{bool(1.0)=}")
print(f"{bool(-1.0)=}")

# строки

print(f"{bool('')=}")
print(f"{bool(' ')=}")
print(f"{bool('hello')=}")

# Списки (Lists)
print(f'{bool([])=}')  # Пустой список
print(f'{bool([1, 2, 3])=}')  # Непустой список

# Кортежи (Tuples)
print(f'{bool(())=}')  # Пустой кортеж
print(f'{bool((1, 2))=}')  # Непустой кортеж

# Словари (Dictionaries)
print(f'{bool({})=}')  # Пустой словарь
print(f'{bool({"a": 1})=}')  # Непустой словарь

# Множества (Sets)
print(f'{bool(set())=}')  # Пустое множество
print(f'{bool({1, 2, 3})=}')  # Непустое множество

# None
print(f'{bool(None)=}')
"""
# Операторы сравнения

a = 1
b = "1"

print(f"{a == b=}")
print(f"{a <= int(b)=}")
print(f"{str(a) <= b=}")

# да/нет в F-string без ветвления
"""
1. Введите ваше имя
2. Введите ваш возраст
3. Превратите в int возраст int(age)
4. Сделайте форматированную строку с помощью f-string где будет проверка на то, что возраст больше или равен 18 f'{age>=18}'
5. Выведите результат на экран
"""

# name = input("Введите ваше: ")
# age = int(input("Введите ваш возраст: "))
# stroka = f"{age >= 18}"
# print(f"{name} ты совершенолетний {stroka}")

# логические операторы в порядке приоритета

# () - групировка
# in - проверка на вхождение
# not - отрицание
# and - логическое И
# or - логическое ИЛИ


print(f"{not True=}")
print(f"{not False=}")
print(f"{True and True=}")
print(f"{True and False=}")
print(f"{False and True=}")
print(f"{False and False=}")
print(f"{True or True=}")
print(f"{True or False=}")
print(f"{False or True=}")
print(f"{False or False=}")

# комбинация операций
print(f"{True and not True=}") #false
print(f"{True and not False=}") #true
print(f"{True and True and (True or False or False)=}") #true

MAX_THERESHOLD = 100
MIN_THERESHOLD = 50
num = 60

print(num >= MIN_THERESHOLD and num <= MAX_THERESHOLD)

print(MIN_THERESHOLD <= num <= MAX_THERESHOLD)