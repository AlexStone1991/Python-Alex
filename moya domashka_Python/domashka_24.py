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

