"""
"""

from marvel import simple_set, small_dict, full_dict

# Пересоберем сет

new_simple_set = set()

for film in simple_set:
    new_simple_set.add(film)

new_simple_set = {film for film in simple_set}
print(new_simple_set)

# cls - команда терминала для очистки экрана

new_simple_list = []

for film in simple_set:
    if len(film) > 10:
        new_simple_list.append(film.replace(' ', ''))


new_simple_list = [film.replace(' ', '') for film in simple_set if len(film) > 10]

print(new_simple_list)

# Вспомним тернарный IF
a = 5
b = True if a < 10 else False

# Если длина фильма больше 10 берем в обработку. Если содержит "Безымянный" - записываем его как None иначе как есть

new_simple_list = []

for film in simple_set:
    if len(film) > 10:
        if "безымянный" in film.lower():
            new_simple_list.append(None)
        else:
            new_simple_list.append(film)


# Если длина фильма больше 10 берем в обработку. Если содержит "Безымянный" - записываем его как None иначе как есть
new_simple_list = [film if "безымянный" not in film.lower() else None for film in simple_set if len(film) >10]

# Если длина фильма больше 10 берем в обработку. Если содержит "Безымянный" - записываем его как None иначе как есть/
# Хочу чтобы безымянные фильмы обрабатывались все вне зависимости от длины
new_simple_list = [
    film if "безымянный" not in film.lower() else None
    for film in simple_set
    if len(film) > 10 or "безымянный" in film.lower()
]

# Small dict - переходим на словари

films =list(small_dict.keys())
print(films)

films = []

for film in small_dict.keys():
    films.append(film.replace(" ", ""))


# Делаем список ключей и реплейс проблеа на ничего
films = [film.replace(" ", "") for film in small_dict.keys()]


# Просто бересоберем словарь

new_small_dict = {}

for film, year in small_dict.items():
    new_small_dict[film] = year


new_small_dict = {film: year for film, year in small_dict.items()}


# Получим на выходе словарь. НО! В значениях вместо None будет 0
new_small_dict = {}

for film, year in small_dict.items():
    if year is None:
        new_small_dict[film] = 0
    else:
        new_small_dict[film] = year

new_small_dict = {film: year if year is not None else 0 for film, year in small_dict.items()}
print(new_small_dict)


# Переходим на marvel full_dict
# Обход словаря словарей и на сколько сложно добраться до нужных данных
# for id, film in full_dict.items():
    # print(id, film)
    # Хочу добраться до названия фильма
    # print(film["title"])


# Перепакуем в список словарей.

full_marvel = []

for id, film in full_dict.items():
    new_dict = {
        "id": id,
        **film
    }
    full_marvel.append(new_dict)

from pprint import pprint


full_marvel = [{"id": id, **film} for id, film in full_dict.items()]
pprint(full_marvel, sort_dicts=False)


# Получили удобную коллекцию. Продолжим работать с full_marvel
# Пройдем по фильмам, и year TBA поменяем на 0

new_full_marvel = []

for film in full_marvel:
    if film["year"] == "TBA":
        film["year"] = 0
    new_full_marvel.append(film)


new_full_marvel = [
    film if film["year"] != "TBA" else {**film, "year": 0} for film in full_marvel
]

print(new_full_marvel)
# pip install tabulate

from tabulate import tabulate

print(tabulate(new_full_marvel, headers="keys", tablefmt="grid"))

# запишем это в html файл
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
        <title>Список студентов</title>
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


input("Нажмите Enter для выхода")


##### Try - Except - Else - Finally

a = 1
b = "2"

if not isinstance(a, int):
    raise TypeError("a должен быть int")

if not isinstance(b, int): # TypeError: b должен быть int
    raise TypeError("b должен быть int")

    

# a / b   # ZeroDivisionError: division by zero

try:
    a / b

except ZeroDivisionError:
    print("Деление на ноль")

except TypeError:
    print("Неверный тип данных")

else:
    print("Все хорошо")

finally:
    print("Выполнится всегда")
