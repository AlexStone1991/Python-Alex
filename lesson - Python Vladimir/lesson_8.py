"""
Урок 8
15.12.2023

1. Сеты. Хеширование и рандом на практике (орел решка)
2. Методы сетов (анализ коллекции фильмов)
3. Знакомство со словарями
4. Что может быть ключем словаря
5. Хеширование ключей и уникальные записи
6. Создание пустого словаря. Внесение записей
7.

"""

import random
from pprint import pprint
from marvel import small_dict

# PRACTICE Орел Решка на сетах
"""
Подкидываем монетку через while и сеты
1. Сделайте переменную счетчик (опционально, это может быть пользовательским вводом - сколько хотите раз подкинуть монетку)
2. Сделайте цикл while пока счетчик меньше 10
3. Внутри цикла сделайте сет с 2 строками, орел, решка
4. Сделайте принт сет.pop и счетчик + 1
"""
# coin_set = {"орел", "решка"}
# print(coin_set.pop())


THROUGHOUT = 100
coin_list = ["орел", "решка"]
# Счетчики орла и решки
eagle_count = 0
tails_count = 0

for i in range(THROUGHOUT):
    coin = random.choice(coin_list)
    if coin == "орел":
        eagle_count += 1
    else:
        tails_count += 1

    print(coin)

print(f"Орел: {eagle_count}, Решка: {tails_count}")

"""

Давайте разберем полную картину:

В Python строковые литералы (строки в кавычках) интернируются - это значит, что Python повторно использует уже созданные строки вместо создания новых копий. Когда вы пишете {'орел', 'решка'} много раз в цикле, Python не создает новые строки каждый раз, а использует ссылки на уже существующие.

Представьте это как колоду карт:

У вас есть две карты: Туз ♠️ (орел) и Король ♠️ (решка)
Каждый раунд вы:
Берете КОПИИ этих же самых карт (но это те же самые карты, просто новая колода)
Раскладываете их по тем же правилам (хеширование)
Туз всегда ложится слева, потому что его "вес" (хеш) меньше
Король всегда справа
Берете левую карту (pop берет первый элемент по хешу)
И получаете каждый раз Туза!

"""

a = 2.5
print(hash(a))  # 1152921504606846978

b = 4
print(hash(b))  # 4

c = "asfasf1dfsdf#)*"
print(hash(c))  # -2640635771081213618


# Методы сетов
"""
add(item) - добавляет элемент в множество
clear() - удаляет все элементы из множества
copy() - возвращает копию множества
difference(set) - или оператор - возвращает разницу между множествами
difference_update(set) - или оператор -= удаляет элементы из множества, которые есть во втором множестве
discard(item) - удаляет элемент из множества, если он там есть
intersection(set) - или оператор & возвращает пересечение множеств
intersection_update(set) - или оператор &= обновляет множество, оставляя только элементы, которые есть в обоих множествах
isdisjoint(set) - возвращает True, если множества не имеют общих элементов
issubset(set) - возвращает True, если все элементы множества содержатся во втором множестве
issuperset(set) - возвращает True, если все элементы второго множества содержатся в первом множестве
symmetric_difference(set) - или оператор ^ возвращает симметричную разность множеств (элементы, которые есть только в одном из множеств)
symmetric_difference_update(set) - или оператор ^= обновляет множество, оставляя только элементы, которые есть только в одном из множеств
union(set) - или оператор | возвращает объединение множеств
update(set) - или оператор |= обновляет множество, добавляя элементы из другого множества
"""

new_set = {}  # это не сет, это словарь
new_set = set()

# add - добавляет элемент в множество
new_set.add("хлеб")
new_set.add("хлеб")
new_set.add("хлеб")
new_set.add("коньяк")

print(new_set)

# discard - удаляет элемент из множества, если он там есть
new_set.discard("коньяк")
print(new_set)

my_movies = {
    "Терминатор",
    "Матрица",
    "Начало",
    "Гладиатор",
    "Бойцовский клуб",
    "Престиж",
    "Интерстеллар",
}
wife_movies = {
    "Титаник",
    "Дневник памяти",
    "Престиж",
    "Интерстеллар",
    "Ла-Ла Ленд",
    "Гордость и предубеждение",
}

# difference - или оператор - возвращает разницу между множествами
print(
    my_movies - wife_movies
)  # {'Начало', 'Терминатор', 'Гладиатор', 'Матрица', 'Бойцовский клуб'}

# intersection - или оператор & возвращает пересечение множеств
print(my_movies & wife_movies)  # {'Интерстеллар', 'Престиж'}


# symmetric_difference - или оператор ^ возвращает симметричную разность множеств (элементы, которые есть только в одном из множеств)
print(my_movies ^ wife_movies)
# {'Матрица', 'Гордость и предубеждение', 'Титаник', 'Дневник памяти', 'Терминатор', 'Гладиатор', 'Ла-Ла Ленд', 'Бойцовский клуб', 'Начало'}

# union - или оператор | возвращает объединение множеств
print(my_movies | wife_movies)
# {'Бойцовский клуб', 'Ла-Ла Ленд', 'Матрица', 'Престиж', 'Дневник памяти', 'Титаник', 'Начало', 'Терминатор', 'Гордость и предубеждение', 'Гладиатор', 'Интерстеллар'}

# isdisjoint - возвращает True, если множества не имеют общих элементов
print(my_movies.isdisjoint(wife_movies))  # False

# Все четные числа от 2 до 10
all_even = {2, 4, 6, 8, 10}

# Четные числа до 6
small_even = {2, 4, 6}

# Проверяем является ли small_even подмножеством all_even
print(small_even.issubset(all_even))  # True

# Проверяем является ли all_even надмножеством small_even
print(all_even.issuperset(small_even))  # True


# СЛОВАРИ - dict
# Словарь - это упорядоченная коллекция данных, состоящая из пар ключ-значение.

some_dict = {}
some_dict = dict()

some_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
}

person_dict = {
    "name": "Никита",
    "age": 20,
    "is_student": True,
}

# Добавим запись
person_dict["is_married"] = False

person_dict["age"] = 21

print(person_dict)

# PRACTICE - проверка на палиндром резульат в Словарь
words = ["мадам", "топот", "test"]
palindromes = {}
"""
Напишите программу, которая находит все палиндромы в списке и сохраняет их в словаре, где ключом будет исходное слово, а значением - bool.
"""

# for word in words:
#     if word == word[::-1]:
#         palindromes[word] = True
#     else:
#         palindromes[word] = False


for word in words:
    palindromes[word] = word == word[::-1]

palindromes = {word: word == word[::-1] for word in words}


palindromes = []

for word in words:
    result = {
        "word": word,  # ключ word - значение это исходное слово
        "is_palindrome": word == word[::-1],  # результат
    }
    palindromes.append(result)


pprint(palindromes)

person_dict = {
    "name": "Никита",
    "age": 20,
    "is_student": True,
}

print(person_dict)
# {'name': 'Никита', 'age': 20, 'is_student': True}


pprint(person_dict)
# {'age': 20, 'is_student': True, 'name': 'Никита'}


pprint(person_dict, sort_dicts=False)
# {'name': 'Никита', 'age': 20, 'is_student': True}

# Методы словарей
"""
len(dict) - возвращает количество элементов в словаре
for - итерация по ключам словаря
in - проверяет, есть ли ключ в словаре
get(key, default=None) - возвращает значение ключа, если ключ существует, иначе возвращает default
items() - возвращает пары ключ-значение в виде списка кортежей
keys() - возвращает список ключей
values() - возвращает список значений
update(other) - обновляет словарь, добавляя пары ключ-значение из other
clear() - удаляет все элементы из словаря
copy() - возвращает копию словаря
fromkeys(iterable, value=None) - возвращает словарь с ключами из iterable и значением value
pop(key, default=None) - удаляет ключ и возвращает значение, если ключ существует, иначе возвращает default
popitem() - удаляет и возвращает последнюю пару ключ-значение
setdefault - возвращает значение ключа, если ключ существует, иначе добавляет ключ с значением default
"""

person_dict = {
    "name": "Никита",
    "age": 20,
    "is_student": True,
}

person_dict["is_married"] = False
person_dict["age"] = 21
person_dict["hobbies"] = ["чтение", "программирование", "путешествия"]

new_data = {
    "is_married": True,
    "hobbies": ["чтение", "программирование", "путешествия"],
    "age": 22,
}

person_dict.update(new_data)
person_dict.update(
    {
        "favorite_color": "white",
    }
)

pprint(person_dict, sort_dicts=False)
print(len(person_dict))
print("name" in person_dict)

# print(person_dict["nome"]) # KeyError: 'nome'
print(person_dict.get("nome"))  # вернет None или значение, указанное вторым аргументом


pprint(small_dict, sort_dicts=False)

# for film in small_dict.keys():
#     print(film)

# keys - возвращает список ключей
# values - возвращает список значений
# items - возвращает список пар ключ-значение

for film, year in small_dict.items():
    print(film, year)

# PRACTICE - вывести фильмы из словаря
"""
Попробуйте распечатать фильмы 2024 года
Попробуйте найти фильмы где есть "чел" в названии
"""
print("--------------------------")

for film, year in small_dict.items():
    if year == 2024:
        print(film)
    if "чел" in film.lower():
        print(film)


print(type(small_dict.keys()))  # <class 'dict_keys'>
print(type(small_dict.values()))  # <class 'dict_values'>
print(type(small_dict.items()))  # <class 'dict_items'>

print(small_dict.keys())
print(small_dict.values())
print(small_dict.items())

[
    ("Железный человек", 2008),
    ("Невероятный Халк", 2008),
    ("Железный человек 2", 2010),
    ("Тор", 2011),
    ("Первый мститель", 2011),
    ("Мстители", 2012),
]

dict_items = [("Железный человек", 2008)]
film, year = dict_items[0]


import os

USER_DICT = r"C:\Users\user\Pictures"
RESULT_DICT = {}

# Итерируемся по файлам в директории и записываем в словарь
# количество папок, и количество файлов по расширениям
# На выходе получим словарь вида:
# RESULT_DICT = {
#     "jpg": 5,
#     "png": 10
#     "fodler": 10
#     ...

"""
Методы OS которые тут могут подойти
os.path.isdir(path) - проверяет, является ли путь директорией
os.path.isfile(path) - проверяет, является ли путь файлом
os.listdir - возвращает список файлов и директорий в указанной директории
walk - обходит все директории в указанной директории и возвращает список файлов и директорий в каждой директории
"""

for file in os.listdir(USER_DICT):
    if os.path.isdir(file):
       RESULT_DICT['folder'] = RESULT_DICT.get('folder', 0) + 1
    else:
        file_ext = os.path.splitext(file)[1]
        RESULT_DICT[file_ext] = RESULT_DICT.get(file_ext, 0) + 1

print(RESULT_DICT)
