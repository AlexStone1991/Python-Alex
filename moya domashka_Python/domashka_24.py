from marvel import full_dict
from pprint import pprint
from typing import Dict, List, Set, Any

# Шаг 2: Ввод от пользователя
user_input = input("Введите цифры через пробел: ")
processed_input = list(map(lambda x: int(x) if x.isdigit() else None, user_input.split()))
print("Обработанный ввод:", processed_input)

# Шаг 3: Перепаковка full_dict
repacked_list = [{"id": key, **value} for key, value in full_dict.items()]
print("Перепакованный список словарей:", repacked_list[:2])

# Шаг 4: Фильтрация по id
filtered_list = list(filter(lambda x: x["id"] in processed_input, repacked_list))
print("Отфильтрованный список:", filtered_list)

# Шаг 5: Множество уникальных режиссеров
unique_directors = {movie["director"] for movie in full_dict.values()}
print("Уникальные режиссеры:", unique_directors)

# Шаг 6: Преобразование года в строку (опционально)
year_as_string = {key: {**value, "year": str(value["year"])} for key, value in full_dict.items()}
print("Год как строка:", year_as_string[list(year_as_string.keys())[0]])

# Шаг 7: Фильтрация фильмов, начинающихся на "Ч"
filtered_by_title = list(filter(lambda x: x["title"].startswith("Ч"), full_dict.values()))
print("Фильмы, начинающиеся на 'Ч':", filtered_by_title)

# Шаг 8: Сортировка по году выпуска
sorted_by_year = dict(sorted(full_dict.items(), key=lambda x: x[1]["year"]))
print("Сортировка по году выпуска:", sorted_by_year[list(sorted_by_year.keys())[0]])

# Шаг 9: Сортировка по году и названию
sorted_by_year_and_title = dict(sorted(full_dict.items(), key=lambda x: (x[1]["year"], x[1]["title"])))
print("Сортировка по году и названию:", sorted_by_year_and_title[list(sorted_by_year_and_title.keys())[0]])

# Шаг 10: Однострочник для фильтрации и сортировки
filtered_and_sorted = dict(sorted(filter(lambda x: x[1]["year"] > 2000, full_dict.items()), key=lambda x: x[1]["title"]))
print("Отфильтрованные и отсортированные фильмы:", filtered_and_sorted)

# Шаг 12: Красивый вывод с pprint
print("\nРезультаты задания:")
pprint(filtered_and_sorted)