# TODO Функции. Ч4.Работа с файлами.TXT CSV JSON YAML. Урок 17.

# ФЛаги
# r -  открывает файл только для чтения - падает с ошибкой если файла нет
# w - открывает файл для записи - создает файл если его нет
# a - открывает файл для добавления данных - создаст файл если его нет
# b - открыть файл в бинарном режиме

# Список функций для TXT
# open() - открывает файл и возвращает итератор
# read() - прочитать весь файл - возвращает строку с содержимым всего файла. Если файл большой, может занять много памяти
# readline() - прочитать одну строку - возвращает строку до символа переноса строки \n. При повторном вызове читает следующую строку
# readlines() - прочитать все строки и вернуть список строк - каждый элемент списка это отдельная строка с \n в конце
# write() - записать данные в файл - принимает строку, возвращает количество записанных символов. Не добавляет \n автоматически
# writelines() - записать список строк в файл - принимает список строк, не добавляет \n между строками автоматически. Нужно добавлять самостоятельно
# close() - закрывает файл и освобождает ресурсы. Важно всегда закрывать файлы после работы

# with open("lesson_17.txt", "w", encoding="utf-8") as file:
#     file.write("Hello, world!\n")
#     file.write("Привет, мир!\n")

# JSON - JavaScript Object Notation
import json

metallica_songs = [
    {
        "name": "Nothing Else Matters",
        "author": "James Hetfield, Lars Ulrich",
        "year": 1991,
        "duration": 390,  # 6 минут 30 секунд
        "description": "Одна из самых известных баллад Metallica, написанная Джеймсом Хэтфилдом. Песня о доверии и преданности.",
    },
    {
        "name": "Enter Sandman",
        "author": "James Hetfield, Lars Ulrich, Kirk Hammett",
        "year": 1991,
        "duration": 332,  # 5 минут 32 секунды
        "description": "Хит из альбома 'Metallica', ставший визитной карточкой группы. Песня о кошмарах и страхах.",
    },
    {
        "name": "Master of Puppets",
        "author": "James Hetfield, Lars Ulrich, Kirk Hammett, Cliff Burton",
        "year": 1986,
        "duration": 515,  # 8 минут 35 секунд
        "description": "Эпическая композиция из одноимённого альбома, классика трэш-метала. Песня о зависимости и контроле.",
    },
]

new_data = [
    {
        "name": "One",
        "author": "James Hetfield, Lars Ulrich",
        "year": 1988,
        "duration": 446,  # 7 минут 26 секунд
        "description": "Мощная песня из альбома '...And Justice for All', известная своим социальным посылом. Песня о войне и её последствиях.",
    },
    {
        "name": "Fade to Black",
        "author": "James Hetfield, Lars Ulrich, Kirk Hammett, Cliff Burton",
        "year": 1984,
        "duration": 420,  # 7 минут 0 секунд
        "description": "Лирическая композиция из альбома 'Ride the Lightning', одна из первых баллад группы. Песня о депрессии и потере смысла жизни.",
    },
]

# 4 метода для работы с JSON
# dump - записывает данные в файл
# dumps - возвращает строку
# load - читает данные из файла
# loads - возвращает словарь

json_string = json.dumps(metallica_songs, indent=4, ensure_ascii=False) # Разбил красиво на колонки
back_data = json.loads(json_string) # возращает список словарей

# записали
with open("metallica_songs.json", "w", encoding="utf-8") as file: # encoding="utf=8" - указывать нужно всегда
    json.dump(metallica_songs, file, indent=4, ensure_ascii=False) # ensure_ascii=False - что б русские буквы читались!

# Дозапись
# 1. Читаем
with open("metallica_songs.json", "r", encoding="utf=8") as file:
    data = json.load(file)

# 2. Добавляем новые песни
data.extend(new_data)

# 3. Перезаписываем файл
with open("metallica_songs.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

# 4. Проверяем
# Прочитали
with open("metallica_songs.json", "r", encoding="utf-8") as file:
    data = json.load(file)

print(data)

