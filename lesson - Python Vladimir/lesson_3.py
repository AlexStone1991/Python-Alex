"""
Lesson 3
Математика в Python
Базовые математические операции. Округление. Библиотека random


Lesson 3
01.12.2023

- Базовые математические операции
    - Сложение, вычитание, умножение, деление
    - Целочисленное деление //
    - Остаток от деления %
    - Возведение в степень **
    - Приоритет операций
    - Скобки для изменения приоритета

- Библиотека random
    - Случайное целое число randint()
    - Случайное число с плавающей точкой random()
    - Случайный выбор choice()
    - Перемешивание списка shuffle()
    - Случайная выборка sample()



- Работа с числами
    - Преобразование строк в числа (int(), float())
    - Математические функции (, round())
    - Округление round()
        - round() с указанием точности



- Практические примеры
    - Калькулятор
    - Игра "Угадай число"
    - Генератор случайных паролей

    
#TODO - Проект "Поле Чудес" с рандомом и строками (и срезами)
# TODO - Проект "Шифровальщик" - перемешивает все буквы кроме первой и последней
#TODO - Проект "Холодно - Горячо" с загадыванием числа компьютером

----------------------
Булева логика. 
Какие типы данных что возвращают?
Операторы сравнения
"""

# Базовые математические операции
# Сложение a + b
# Вычитание a - b
# Умножение a * b
# Деление a / b
# Целочисленное деление a // b
# Остаток от деления a % b
# Возведение в степень a ** b

# Приоритет операций
# 2 + 2 * 2 = 6
# (2 + 2) * 2 = 8

# input - ввод данных в консоль, он всегда возвращает строку

# a = input('Введите первое число: ')
# b = input('Введите второе число: ')

# a = int(a)
# b = int(b)

# c = int(input('Введите третье число: '))

# print(f'{a+b=}')
# print(f'{a+b*c=}')
# print(f'{(a+b)*c=}')

# Целочисленное деление //
# Остаток от деления %

"""
1. Введите количество гостей
2. Введите сколько человек помещается в один автобус
3. Вывести сколько автобусов нужно заказать (используя целочисленное деление)
4. Вывести сколько человек останется (используя остаток от деления)
"""

# guests = int(input('Введите количество гостей: '))
# seats_in_bus = int(input('Введите сколько человек помещается в один автобус: '))

# buses = guests // seats_in_bus
# guests_left = guests % seats_in_bus

# print(f'Количество наполненных автобусов: {buses}\nВсего автобусов: {buses + 1}\nОсталось гостей: {guests_left}')
print(f"{2**2=}")
print(f"{2**3=}")
print(f"{2**4=}")

# Import random
# import random # при обращении к модулю random мы получаем объект модуля и все функции модуля. Вызов random.chose
from random import randint, random, choice, shuffle, sample # импортируем конкретные функции из модуля random. Вызов randint

# randint(a, b) - случайное целое число от a до b включительно
# random() - случайное число от 0 до 1
# choice(seq) - случайный элемент из последовательности seq
# shuffle(seq) - перемешивает последовательность seq
# sample(population, k) - случайная выборка элементов из последовательности population размера k
word = 'Hello'
# Разобьем строку на список
word_list = list(word)
shuffle(word_list)
print(word_list)

print(randint(1, 10))
print(random())
print(choice(word))

# sample
print(sample(word, 3))

"""
Попробуем сделать перемешивание строки через sample
1. Получить у пользователя строку
2. Получить длину строки через len
3. Создать переменную и положить туда результат вызова sample с параметрами sample(строка, длина строки)
4. Применить join к переменной и вывести на экран  " ".join(переменная)
"""
# 1. Получить у пользователя строку
word = input('Введите строку и я перемешаю буквы: ')

# 2. Получить длину строки через len
word_len = len(word)

# 3. Создать переменную и положить туда результат вызова sample с параметрами sample(строка, длина строки)
shuffled_word = sample(word, word_len)

# 4. Join
result = "".join(shuffled_word)
print(result)

############ Float - числа с плавающей точкой

a = 1
print(float(a))

b = 4
c = 2
print(b / c)

# Округление
# round(число, количество знаков после запятой)

d = 11094.22985

print(round(d, 3))
print(round(d, -2))

# Сложение Float
# print(0.1 + 0.2)

from decimal import Decimal

# С использованием float
price = 0.1 + 0.2
print(f'Float: {price}')  # 0.30000000000000004

# С использованием Decimal
price_decimal = Decimal('0.1') + Decimal('0.2')
print(f'Decimal: {price_decimal}')  # 0.3

# При множественных операциях разница становится заметнее
float_sum = sum([0.1] * 1000)
decimal_sum = sum([Decimal('0.1')] * 1000)

print(f'Float sum: {float_sum}')  # 0.9999999999999999
print(f'Decimal sum: {decimal_sum}')  # 1.0



# Как правильно писать флоат
a = 1,3
b = 1.3 # Float, число

#############
# Функция приведения к bool
# bool(value)

# Целые числа
print(f'{bool(0)=}')
print(f'{bool(1-1)=}')
print(f'{bool(1)=}')
print(f'{bool(-1)=}')

# Дробные числа
print(f'{bool(0.0)=}')
print(f'{bool(1.0)=}')
print(f'{bool(-1.0)=}')

# Строки
print(f'{bool("")=}')
print(f'{bool(" ")=}')
print(f'{bool("Hello")=}')


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

##### Операции сравнения
# == - равно
# != - не равно
# > - больше
# < - меньше
# >= - больше или равно
# <= - меньше или равно

a = 1
b = '1'

print(f'{a == b=}')
# print(f'{a < b=}') # TypeError: '<' not supported between instances of 'int' and 'str'
print(f'{a <= int(b)=}')
print(f'{str(a) <= b=}')


# PRACTICE
# ДА\НЕТ в F-string без ветвления
"""
1. Введите ваше имя
2. Введите ваш возраст
3. Превратите в int возраст int(age)
4. Сделайте форматированную строку с помощью f-string где будет проверка на то, что возраст больше или равен 18 f'{age>=18}'
5. Выведите результат на экран
"""

AGE_LIMIT = 18
# 1. Имя
name = input('Введите ваше имя: ')

# 2. Возраст и преобразование в int
age = int(input('Введите ваш возраст: '))

# 4. Собираем форматированную строку
result = f'{name}, Вы совершеннолетний: {age >= AGE_LIMIT}'

# 5. Выводим результат
print(result)

################### Проверка на вхождение в строку
# value in sequence

fast_food_string = 'чебурек бургер пицца суши сало'

user_product = "Бургер"

result = user_product in fast_food_string

print(f'Результат вхождения продукта {user_product} во вредные продукты: {result}')

########## Логические операторы в порядке приоритета
# () - группировка
# not - отрицание
# and - логическое И
# or - логическое ИЛИ

print(f'{not True=}')
print(f'{not False=}')
print(f'{True and True=}')
print(f'{True and False=}')
print(f'{False and True=}')
print(f'{False and False=}')
print(f'{True or True=}')
print(f'{True or False=}')
print(f'{False or True=}')
print(f'{False or False=}')

# Комбинация операций
print(f'{True and not True=}') # False
print(f'{True and not False=}') # True
print(f'{True and True and (False or False or True)=}') # True
print(f'{True and True and False or False or True=}')  


AGE_LIMIT = 18
BLACK_LIST_NAMES = "Вася Петя Маша Вова"
# 1. Имя. title - приведение строку вОва к виду Вова
name = input('Введите ваше имя: ').title()

# 2. Возраст и преобразование в int
age = int(input('Введите ваш возраст: '))

# 4. Собираем форматированную строку
result = f'{name}, Можете ли вы войти: {age >= AGE_LIMIT and name not in BLACK_LIST_NAMES}'

print(result)

# Проверка вхождения числа в диапазон

# 1. Через and
MAX_THRESHOLD = 100
MIN_THRESHOLD = 50
num = 60

print(num >= MIN_THRESHOLD and num <= MAX_THRESHOLD)

# 2. Через "ёлочку"
print(MIN_THRESHOLD <= num <= MAX_THRESHOLD)