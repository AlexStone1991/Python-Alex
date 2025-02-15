# TODO Функции Ч8. Генераторы. Генераторные выражения. Урок 21

# Концепция ленивых вычислений
# сравнение range в списке и вне
from typing import Generator
# START_VALUE = 0

# END_VALUE = 1_000_000_000_000_000_000

# range_obj = range(START_VALUE, END_VALUE)

# # Помещаем это в фильтр для получения только четных чисел. получаем обьет фильтра.
# even_numbers = filter(lambda x: x % 2 == 0, range_obj)

# # получаем map обьект из even_numbers и превращаем числа в строки добаляем число
# even_numbers_str = map(lambda x: f"число: {x}", even_numbers)

# for num in even_numbers_str:
#     print(num)
from pprint import pprint
from cities import cities_list



from typing import Generator
from urllib import response


print(len(cities_list))
pprint(sorted(cities_list, key=lambda x: x["population"], reverse=True)[:5])

# Получим названия городов несколькими способами

# 1. Классика. Цикл
cities = []
for city in cities_list:
    cities.append(city["name"])

# 2. Списковое выражение
cities = [city["name"] for city in cities_list]

# 3. Генераторная функция


def get_cities_gen(cities: list[dict]) -> Generator[str]:
    for city in cities:
        yield city["name"]


cities_gen = get_cities_gen(cities_list)

# 4. Генераторное выражение

cities_gen = (city["name"] for city in cities_list)
# 5. Поместим это в фильтр - нужны города начинающиеся на Й
# filtered_cities = (city["name"] for city in cities_list if city["name"].startswith("Ш"))

# for city in filtered_cities:
#     print(city)

# 5. В ленивом режиме запишем имена в cities.txt
file_name = "cities.txt"

with open(file_name, "w", encoding="utf-8") as f:
    for city in cities_gen:
        f.write(f"{city}\n")


# Построчное чтение - возвращаем генератор
# with open(file_name, "r", encoding="utf-8") as f:
#     # for line in f:
#     #     print(line.strip())
#     cities = (line.strip() for line in f)

#     # Получим города где есть тире
#     filtered_cities = (city for city in cities if "-" in city)


def read_file_lines(filename: str) -> Generator[str]:
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            yield line.strip()


cities = read_file_lines(file_name)

for city in cities:
    print(city)





# list_range = list(range(START_VALUE, END_VALUE)) # MemoryError

# range_object = range(START_VALUE, END_VALUE)
# print(range_object, type(range_object))

# for num in range_object:
#     print(num) # будет бесконечность чисел

# Генераторы функции. Yield.


# potatos = ["картошка", "картошка", "гнилая картошка", "картошка"]

# def clean_potatos(potatos: list[str]) -> list[str]:
#     new_potatos = []

#     for potato in potatos:
#         potato += "_чищенная"
#         new_potatos.append(potato)
#     return new_potatos

# cleaned_potatos = clean_potatos(potatos)

# print(cleaned_potatos)

# # Генераторные функции. Yield

# def generator_clean_potatos(potatos: list[str]) -> Generator[str]:
#     for potato in potatos:
#         yield potato + "_чищенная"
#         yield potato

# cleaned_potatos = generator_clean_potatos(potatos)
# print(next(cleaned_potatos))
# print(next(cleaned_potatos))
# print(next(cleaned_potatos))

# for potato in cleaned_potatos:
#     print(potato, "Из цикла")

# for potato in generator_clean_potatos(potatos):
#     print(potato, "Из цикла_2")