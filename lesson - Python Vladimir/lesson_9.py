"""
Python: Разбор HW. Словари и обработка данных. Урок: 9
21.12.2024

- Разбор домашнего задания: +
    - Генератор пословиц
    - Разбор типовых ошибок
    - Оптимизация решений

- Углубленная работа со словарями:
    - Вложенные словари и их структура
    - Обработка сложных структур данных
    - List comprehension для словарей
    - Dictionary comprehension

- Практика со словарями:
    - Работа с JSON-подобными структурами
    - Трансформация и обработка данных
    - Агрегация и группировка
    - Фильтрация по сложным условиям

- Проекты:
    1. Анализатор текста:
        - Подсчет частоты слов
        - Создание словаря синонимов
        - Статистика использования слов

    2. Управление данными пользователей:
        - Создание структуры данных
        - CRUD операции
        - Валидация данных
        - Поиск и фильтрация

    3. Работа с вложенными структурами:
        - Парсинг сложных словарей
        - Обновление вложенных значений
        - Объединение словарей
        - Форматированный вывод
"""

# Методы словарей


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

# keys() - возвращает список ключей
# values() - возвращает список значений
# values() - возвращает список значений

from marvel import small_dict, full_dict
from pprint import pprint

marvel_keys = small_dict.keys()
marvel_values = small_dict.values()
marvel_items = small_dict.items()

# print(marvel_keys[:3]) # TypeError: 'dict_keys' object is not subscriptable
# print(marvel_values[:3])
# print(marvel_items[:3])

# print(list(marvel_keys)[:3])  # TypeError: 'dict_keys' object is not subscriptable
# print(list(marvel_values)[:3])
# print(list(marvel_items)[:3])

# one_item = list(marvel_items)[0]
# print(one_item)
# print(type(one_item))  #  tuple

# ('Железный человек', 2008)
# film, year = one_item

# Кортеж - неизменяемый список
# tuple - кортеж
# some_tuple = (1, 2, 3)
# typle_nums = 1,2

# for key, value in small_dict.items():
#     print(key, value)


# empty_dict = {}


# person_dict = {
#     "name": "Никита",
#     "age": 20,
#     "is_student": True,
# }

# person_dict["is_married"] = False
# person_dict["age"] = 21
# person_dict["hobbies"] = ["чтение", "программирование", "путешествия"]

# new_data = {
#     "is_married": True,
#     "hobbies": ["чтение", "программирование", "путешествия"],
#     "age": 22,
# }

# person_dict.update(new_data)
# person_dict.update(
#     {
#         "favorite_color": "white",
#     }
# )

# film = "Железный человек 4"

# Попытаюсь добыть его
# print(small_dict[film])  #  KeyError: 'Железный человек 4'

# Попробуем получить значение по ключу (Второй аргумент не обязательный)
# print(small_dict.get(film))  # None

# Посмотрел фильм Блэйд
# print(small_dict.get("Блэйд")) # 2025
# print(small_dict.pop("Блэйд"))  # Удалили фильм
# print(small_dict.popitem())  # Удалили фильм
# print(small_dict.get("Блэйд"))  # None

# Попробуем перепаковать full_dict в список словарей

# pprint(full_dict, sort_dicts=False)
# print(full_dict.keys())

# pprint(list(full_dict.values()), sort_dicts=False)

# result = []

# for id, film in full_dict.items():
#     film["id"] = id
#     result.append(film)

result = []

for id, film in full_dict.items():
    new_dict = {
        "id": id,
        "title": film["title"],
        "year": film["year"],
        "director": film["director"],
        "screenwriter": film["screenwriter"],
        "producer": film["producer"],
        "stage": film["stage"],

    }
    result.append(new_dict)

result = []

for id, film in full_dict.items():
    new_dict = {
        "id": id
    }
    new_dict.update(film)
    result.append(new_dict)


films_collection = []

for id, film in full_dict.items():
    new_dict = {
        "id": id,
        **film
    }
    films_collection.append(new_dict)

pprint(result, sort_dicts=False)


# PRACTICE - ищем информацию о фильме
"""
1. Делаем пользовательский ввод
2. Объявляем цикл по films_collecton (список словарей)
for film in film_collection:
- Доступ к названию будет через film["title"]
Надо найти фильм с таким названием
И вывести по нему информацию f'{film["title"]} - {film["year"]}'
Сделайте break, если фильм найден
Под блоком for сделайте блок else
куда мы попадем, если в циикле не было break
там сделайте принт, что фильм не найден
"""

# # Простой вариант
# user_film = input("Введите название фильма: ").strip()
# for film in films_collection:
#     if film["title"] == user_film:
#         print(f'{film["title"]} - {film["year"]}')
#         break
# else:
#     print(f'Фильм "{user_film}" не найден')



# Вариант с поиском с поправкой на разный регистр пробелы и знаки препинания

# user_film = input("Введите название фильма: ")
# row_user_film = user_film.lower().replace(" ", "").replace(".", "").replace(",", "")

# for film in films_collection:
#     # Приводим название фильма к одному регистру и убираем пробелы, точки и запятые

#     row_film_title = film["title"].lower().replace(" ", "").replace(".", "").replace(",", "")
    
#     if row_film_title == row_user_film:
#         print(f'{film["title"]} - {film["year"]}')
#         break

# else:
#     print(f'Фильм "{user_film}" не найден')



# Вариант где мы ищем все похожие фильмы

result = []
print(f'Печатаем {films_collection}')
user_film = input("Введите название фильма: ")
row_user_film = user_film.lower().replace(" ", "").replace(".", "").replace(",", "")

for film in films_collection:
    # Приводим название фильма к одному регистру и убираем пробелы, точки и запятые
    
    if film['title']:
    
        row_film_title = film["title"].lower().replace(" ", "").replace(".", "").replace(",", "")

        if row_user_film in row_film_title:
            film = {
                "title": film["title"],
                "year": film["year"],
                "stage": film["stage"],
            }

            result.append(film)


if result:
    print(f"Найдено {len(result)} фильмов:")
    [print(film) for film in result]
else:
    print(f'Фильм "{user_film}" не найден')
