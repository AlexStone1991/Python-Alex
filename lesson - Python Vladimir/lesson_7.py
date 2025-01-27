"""
Урок 7
14.12.2023

Методы списков:
- append(), extend(), insert() 
- remove(), pop(), clear() 
- index(), count() 
- sort(), reverse() 
- copy() 

Практика со списками:
- Работа с вложенными списками-
- Сортировка списков разными способами+
- Удаление дубликатов(+ -)
- Объединение списков -
- Фильтрация элементов -

Множества (set):
- Создание множеств +
- Операции с множествами -
- Методы множеств -
- Практическое применение -

Хеширование: +
- Понятие хеш-функции 
- hash() встроенная функция 
- Применение хеширования 

Проекты: +++
1. Игра "Камень, ножницы, бумага":
   - Ввод пользователя
   - Генерация хода компьютера
   - Определение победителя
   - Подсчет очков
   - Повторение игры

2. Работа со списками покупок:
   - Добавление/удаление элементов
   - Сортировка по категориям
   - Поиск дубликатов
   - Объединение списков

3. Анализ данных с помощью множеств:
   - Поиск уникальных элементов
   - Пересечение данных
   - Разность множеств
"""

"""
Методы и функции для работы с списками:
len(list) - возвращает длину списка
max(list) - возвращает максимальный элемент списка
min(list) - возвращает минимальный элемент списка
sum(list) - возвращает сумму элементов списка
sorted(list) - возвращает новый отсортированный список
bool(list) - возвращает True, если список не пустой, и False, если список пустой


list.append(item) - добавляет элемент в конец списка
list.extend(iterable) - добавляет элементы из итерируемого объекта в конец списка
list.insert(index, item) - вставляет элемент по указанному индексу
list.remove(item) - удаляет первый элемент со значением item из списка
list.pop(index) - удаляет элемент по указанному индексу и возвращает его
list.clear() - удаляет все элементы из списка
list.index(item) - возвращает индекс первого элемента со значением item
list.count(item) - возвращает количество элементов со значением item в списке
list.sort() - сортирует список по возрастанию
list.reverse() - разворачивает список
"""

# names_list = ["Антон", "Анна", "Андрей", "Алексей", "Анастасия"]
# names_list.sort()
# print(names_list)

# print(max(names_list))
# print(min(names_list))

# # Сортировка списка по длине имени
# names_list.sort(key=len, reverse=True)
# print(names_list)

# # Список чисел
# nums_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(sum(nums_list))
# print(max(nums_list))
# print(min(nums_list))

# # Нам надо понять есть ли имена длиннее 10 символов

# is_long_name = False

# for name in names_list:
#     if len(name) >= 10:
#         is_long_name = True
#         print("Есть длинные имена")
#         break
# else:
#     print("Нет длинных имен")

# long_name = [name for name in names_list if len(name) >= 10]
# if long_name:
#     print("Есть длинные имена")
# else:
#     print("Нет длинных имен")

# # Добавление в список
# # append() - добавляет элемент в конец списка
# # extend() - добавляет элементы из итерируемого объекта в конец списка
# # insert() - вставляет элемент по указанному индексу

# names_list = ["Антон", "Анна", "Андрей", "Алексей", "Анастасия"]
# # Добавление в конец списка
# names_list.append("Елена")

# # Добавление в начало списка
# names_list.insert(0, "Алексей")


# # PRACTICE Практика топ3 имён
# """
# 1. Объявите пустой список names_list
# 2. Объявите цикл while true и в нём получите от пользователя имя
# 3. Если длина списка равна 3 или более - добавьте имя под индексом 0
# 4. Удалите последний элемент списка list.pop()
# 5. Если длина списка меньше 3 - добавьте имя в конец списка
# 6. Выведите список на экран

# """

# user_names = []

# while True:
#     name = input("Введите имя: ")
#     if name == "стоп" or name == "":
#         break

#     if len(user_names) >= 3:
#         user_names.insert(0, name)
#         user_names.pop()
#     else:
#         user_names.append(name)

#     print(user_names)


# """
# list.remove(item)  - удаляет первый элемент со значением item из списка
# list.pop(index)  - удаляет и возвращает элемент с конца или по указанному индексу
# """

# product_list = ["яблоко", "банан", "апельсин", "яблоко", "банан", "яблоко"]
# # Удаление элемента по значению
# product_list.remove("банан")
# print(product_list)
# print(product_list.pop(1))


# product_list_2 = product_list.copy()
# product_list[0] = "киви"
# print(product_list_2)

# Set - множество
# Множество - это неупорядоченная коллекция неизменяемых уникальных элементов.
# Неизменяемые:  строки, числа, кортежи, bool None

"""Хеширование в Сетах. Что это?

Хеширование - это процесс преобразования данных в фиксированный размер, который называется хешем.


"""

# a = "1"
# b = "2"
# c = "3"

# print(hash(a))
# print(hash(b))
# print(hash(c))


"""
5586480241889768794
-4825865226336306730
-1927537420559775290

-1108596424213146015
1320272752365341559
-6483631880240495448

"""

# product_set = {"яблоко", "банан", "апельсин", "яблоко", "банан", "яблоко"}
# print(product_set)
# print(product_set)
# print(product_set)
# print(product_set)

# print(product_set.pop())
# print(product_set.pop())
# print(product_set.pop())
# print(product_set.pop())


#  PRACTICE Камень ножницы бумага
"""

"""
ROUNDS = 5
stone = "бумага"
paper = "ножницы"
scissors = "камень"

variants = ["камень", "ножницы", "бумага"]
results = []
import random

while len(results) < ROUNDS:
    user_choice = input("Введите свой выбор (камень, ножницы, бумага): ")
    computer_choice = random.choice(variants)

    print(f"Вы выбрали {user_choice}, компьютер выбрал {computer_choice}")
    
    if user_choice == computer_choice:
        print("Ничья")
    
    elif user_choice == "камень" and computer_choice == "ножницы":
        print("Вы победили")
        results.append("победа")
    elif user_choice == "ножницы" and computer_choice == "бумага":
        print("Вы победили")
        results.append("победа")
    elif user_choice == "бумага" and computer_choice == "камень":
        print("Вы победили")
        results.append("победа")
    else:
        print("Вы проиграли")
        results.append("поражение")


# Считаем победы
win_count = results.count("победа")
lose_count = results.count("поражение")
# win_count = sum([1 for result in results if result == "победа"])

# Объявляем конечный результат
if win_count > lose_count:
    print("Вы победили")
elif win_count < lose_count:
    print("Вы проиграли")
else:
    print("Ничья")
