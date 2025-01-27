# TODO Словари и обработка данных. Урок 9

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
"""
from marvel import small_dict

marvel_keys = small_dict.keys()
marvel_values = small_dict.values()
marvel_items = small_dict.items()

# print(list(marvel_keys)[:3])
# print(list(marvel_values)[:3])
# print(list(marvel_items)[:3])

# one_item = list(marvel_items)[0]
# print(one_item)
# print(type(one_item))

film, year, = one_item

some_tuple = (1, 2, 3)
tuple_nums = 1,2

for key, value in small_dict.items():
    print(key, value)

empty_dict = {}

person_dict = {
    "name": "Никита",
    "age": 25,
    "is_student": True,
}

person_dict["is_student"] = False
person_dict["age"] = 21
person_dict["hobbies"] = ["Футбол", "програмирование"]

new_data = {
    "is_student": True,
    "hobbies": ["Футбол", "програмирование"],
    "age": 22,
}

person_dict.update(new_data)
person_dict.update(
    {
        "favorite_color": "white",
    }
)

film = "Жлезный человек 4"

# print(small_dict[film]) # KeyError: 'Железный человек 4'

# попробую получить значение по ключу (Второй аргумент не обязательный)
# print(person_dict.get(film)) # NONE

# print(small_dict.get("Блэйд")) # 2025
# print(small_dict.pop("Блэйд")) # Удалили фильм
# print(small_dict.popitem()) # Удалили последний элемент
# print(small_dict.get("Блэйд")) # None
"""

from marvel import small_dict, full_dict
from pprint import pprint

#Попробуем перепаковать full_dict в список словарей

# pprint(small_dict, sort_dicts=False)

# print(full_dict.keys())
# pprint(list(full_dict.values()), sort_dicts=False)

# film_collection = []

# for id, film in full_dict.items():
#     new_dict = {
#         "id": id,
#         **film,
#     }
#     film_collection.append(new_dict)


# pprint(film_collection, sort_dicts=False)

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

user_input = input("Введите название фильма: ").strip()

for film in film_collection:
    if film["title"].lower() == user_input.lower():
        print(f"{film['title']} - {film['year']}")
        break
else:
        print("Фильм не найден")