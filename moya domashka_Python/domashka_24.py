from marvel import full_dict

# Шаг 2: Ввод от пользователя и обработка данных
# Пользователь вводит цифры через пробел. Мы разбиваем строку на список и преобразуем каждый элемент в int. Если элемент не является числом, заменяем его на None.

# Ввод от пользователя
user_input = input("Введите цифры через пробел: ")

# Разбиваем строку на список и преобразуем в int, заменяя нечисловые элементы на None
processed_input = list(map(lambda x: int(x) if x.isdigit() else None, user_input.split()))

print("Обработанный ввод:", processed_input)

# Шаг 3: Перепаковка full_dict в список словарей
# Преобразуем full_dict в список словарей, сохраняя ключ id.

# Перепаковка full_dict в список словарей
repacked_list = [{"id": key, **value} for key, value in full_dict.items()]

print("Перепакованный список словарей:", repacked_list[:2])  # Выводим первые два элемента для примера

# Шаг 4: Фильтрация по id

# Фильтрация по id
filtered_list = list(filter(lambda x: x["id"] in processed_input, repacked_list))

print("Отфильтрованный список:", filtered_list)

# Шаг 5: Множество уникальных режиссеров

# Множество уникальных режиссеров
unique_directors = {movie["director"] for movie in full_dict.values()}

print("Уникальные режиссеры:", unique_directors)

# Шаг 6: Преобразование года в строку
# Создаем копию full_dict, где значение ключа year преобразовано в строку.
# Преобразование года в строку
year_as_string = {key: {**value, "year": str(value["year"])} for key, value in full_dict.items()}

print("Год как строка:", year_as_string[list(year_as_string.keys())[0]])  # Выводим первый элемент для примера

# Шаг 7: Фильтрация фильмов, начинающихся на букву "Ч"
# Используем filter, чтобы оставить только те фильмы, название которых начинается на букву "Ч".

# Фильтрация фильмов, начинающихся на "Ч"
filtered_by_title = list(filter(lambda x: x["title"].startswith("Ч"), full_dict.values()))

print("Фильмы, начинающиеся на 'Ч':", filtered_by_title)
