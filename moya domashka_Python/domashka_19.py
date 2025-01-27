from marvel import small_dict
# Задача 1: Поиск фильмов по названию
user_input = input("Введите название фильма или его часть: ")
user_input_lower = user_input.lower()
found_movies = []

for movie, year in small_dict.items():
    if user_input_lower in movie.lower():
        found_movies.append(movie)
        print(movie)

print("Найденные фильмы:", found_movies)

# Задача 2: Фильтрация фильмов по году выхода
YAER_THRESHOLD = 2024
filtered_movies = []
filtered_dict = {}
filtered_list_of_dicts = []

# Проходим по всем элементам словаря
for movie, year in small_dict.items():
    if year is None:
        continue 
    if year > YAER_THRESHOLD: 
        filtered_movies.append(movie)
        filtered_dict[movie] = year
        filtered_list_of_dicts.append({movie: year})

print("Фильмы, вышедшие после 2024 года:")
print("Список названий:", filtered_movies)
print("Фильтрованный словарь:", filtered_dict)
print("Список словарей:", filtered_list_of_dicts)
