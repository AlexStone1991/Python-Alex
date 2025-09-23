# TODO Словари и однострочники. Урок 10
# cls - команда терминала для очистки экрана

from marvel import simple_set, full_dict, small_dict

# Перебесобираем сет

new_simple_set = set()

for film in simple_set:
    new_simple_set.add(film)

new_simple_set = {film for film in simple_set}# Это тоже самое что и выше однострочный цикл
# print(new_simple_set)

new_simple_list = []

for film in simple_set:
    if len(film) > 10:
        new_simple_list.append(film.replace(" ", ""))

new_simple_list = [film.replace(" ", "") for film in simple_set if len(film) > 10]
# print(new_simple_list)

# Вспоминим тернарный IF
a = 5
b = True if a < 10 else False

# Если фильм содержит "беземянный " записываем его как None

new_simple_list = []

for film in simple_set:
    if len(film) > 10:
        if "безымянный" in film.lower():
            new_simple_list.append(None)
    else:
        new_simple_list.append(film)

# если длина фильма больше 10 берем в обработку если содержит Безымянный - записываем как None иначе как есть
new_simple_list = [film if "безымянный" not in film.lower() else None for film in simple_set if len(film) > 10]
# print(new_simple_list)

# хочу чтобы безымянный фильмы обрабатывались все вне зависимости от длины

new_simple_list = [
    film if "безымянный" not in film.lower() else None
    for film in simple_set
    if len(film) > 10 or "безымянный" in film.lower()]

# Smalll_dict - переходим на свловари

films = list(small_dict.keys())
# print(films)

films = []

for film in small_dict.keys():
    films.append(film.replace(" ", "_"))

# делаем список ключей и реплейс пробела на ничего
films = [film.replace(" ", "_") for film in small_dict.keys()]
# print(films)
# просто пересоберем словарь
# TODO для домашки подойдет!
new_simple_dict = {}
for film, year in small_dict.items():
    new_simple_dict[film] = year

new_simple_dict = {film: year for film, year in small_dict.items()}

# получим на выходе словарь. но в значениях вместоNone будет 0
new_small_dict = {}

for film, year in small_dict.items():
    if year is None:
        new_small_dict[film] = 0
    else:
        new_small_dict[film] = year

new_small_dict = {film: year if year is not None else 0 for film, year in small_dict.items()}
# print(new_small_dict)

# for id, film in full_dict.items():
    # print(id, film)
    # хочу добраться до названия фильма
    # print(film["title"])
from pprint import pprint
# перепакуем в список словарей
full_marvel = []

# for film in full_dict.items():
#     new_dict = {
#         "id": id,
#         **film
#     }
#     full_marvel.append(new_dict)

full_marvel = [{"id": id, **film} for id, film in full_dict.items()]
pprint(full_marvel, sort_dicts=False)

# Поличили удобную коллекцию. продолжим работать с full_marvel
# пройдем по фильмам и year TBA поменяем на 0

new_full_marvel = []

for film in full_marvel:
    if film["year"] == "TBA":
        film["year"] = 0
    new_full_marvel.append(film)

new_full_marvel = [film if film["year"] != "TBA" else {**film, "year": 0} for film in full_marvel]
print(new_full_marvel)

from tabulate import tabulate

print(tabulate(new_full_marvel, headers="keys", tablefmt="grid"))
html_table = tabulate(new_full_marvel, headers="keys", tablefmt="html")

styled_table = html_table.replace(
    '<table>', 
    '<table class="table table-striped table-hover">'
)

html_template = f"""
<!doctype html>
<html lang="ru">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Фильмы Марвел</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>
        <div class="container mt-5">
            <h1 class="mb-4">Фильмы Marvel</h1>
            {styled_table}
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
    </body>
</html>
"""

file = open("marvel.html", "w", encoding="utf-8")
file.write(html_template)
file.close()

input("Нажмите Enter для выхода...")
