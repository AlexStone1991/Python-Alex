# TODO Урок 4. Методы строк. Условные операторы Дебаггер. Срезы Строк.

# условный оператор if
# простой if
# TODO Через Shift tab удаляет отступы

# fast_food_string = "чебурек бургер пицца суши сало"

# user_product = input("Введите название блюда: ")

# if user_product in fast_food_string:
#     print(f"{user_product} Есть в меню")
# else:
#     print(f"{user_product} Нет в меню")

# fast_food_string_ru = "чебурек пирожок булка беляш"
# fast_food_string_en = "бургер попкорн"
# fast_food_string_it = "паста спаггети пицца"
# fast_food_string_mx = "тако тамале начос буррито кесадилья"

# user_product = input("Введите название блюда: ").lower().strip()

# if not user_product.isalpha():
#     print("Такого блюда не существует")

# elif user_product in fast_food_string_ru:
#     print(f"{user_product} Входит в меню русской кухни")

# elif user_product in fast_food_string_en:
#     print(f"{user_product} Входит в меню американской кухни")

# elif user_product in fast_food_string_it:
#     print(f"{user_product} Входит в меню итальянской кухни")

# elif user_product in fast_food_string_mx:
#     print(f"{user_product} Входит в меню мексиканской кухни")

# else:
#     print(f"{user_product} Нет в меню")

# string = "hello world"
# print(id(string))

# string = string.upper()
# print(id(string))

# Методы строк и полезные функции

# - count(substring) - метод возвращает количество вхождений подстроки в строку
# - len(string) - функция возвращает длину строки
# - string.upper() - метод возвращает копию строки в верхнем регистре
# - string.lower() - метод возвращает копию строки в нижнем регистре
# - string.split(sep=None, maxsplit=-1) - метод возвращает список строк, полученный путем разбиения строки по указанному разделителю. maxsplit - максимальное количество разбиений
# - string.join(iterable) - метод возвращает строку, состоящую из элементов итерируемого объекта, соединенных строкой, в которой вызван метод
# - string.capitalize() - метод возвращает копию строки с первым символом в верхнем регистре, а остальные в нижнем
# - string.title() - метод возвращает копию строки с первыми символами каждого слова в верхнем регистре, а остальные в нижнем
# - string.strip([chars]) - метод возвращает копию строки с удаленными указанными символами в начале и конце строки
# - string.lstrip( [chars]) - метод возвращает копию строки с удаленными указанными символами в начале строки
# - string.rstrip( [chars]) - метод возвращает копию строки с удаленными указанными символами в конце строки
# - string.replace(old, new [, count]) - метод возвращает копию строки с замененными указанными символами на новые

# - string.find(sub[, start[, end]]) - метод возвращает индекс первого вхождения подстроки в строке, если подстрока не найдена, возвращает -1
# - string.index(sub[, start[, end]]) - метод возвращает индекс первого вхождения подстроки в строке, если подстрока не найдена, возвращает ValueError
# - string.startswith(prefix[, start[, end]]) - метод возвращает True, если строка начинается с указанной подстроки, иначе False
# - string.endswith(suffix[, start[, end]]) - метод возвращает True, если строка заканчивается указанной подстрокой, иначе False
# - string.isdigit() - метод возвращает True, если все символы в строке являются цифрами, иначе False
# - string.isalpha() - метод возвращает True, если все символы в строке являются буквами, иначе False
# - string.isalnum() - метод возвращает True, если все символы в строке являются буквами или цифрами, иначе False
# - string.islower() - метод возвращает True, если все символы в строке являются строчными буквами, иначе False
# - string.isupper() - метод возвращает True, если все символы в строке являются заглавными буквами, иначе False
# - string.isspace() - метод возвращает True, если все символы в строке являются пробелами, иначе False
# - string.isdecimal() - метод возвращает True, если все символы в строке являются десятичными цифрами, иначе False

# print(f'{"hello".isalpha()=}')
# print(f'{"hello!".isalpha()=}')
# print(f'{"hello ".isalpha()=}')
# print(f'{" ".isalpha()=}')


# print(f"{"hello".isalnum()=}")
# print(f"{"hello!".isalnum()=}")
# print(f"{'hello123'.isalnum()=}")
# print(f"{'!!!!!!!'.isalnum()=}")

# string = "Молоко".replace("о", "а").upper()
# print(string)

# path = input("Введите путь к файлу: ").strip('"').replace(" ", "_")
# print(path)
# input("нажмите Enter для выхода")

# TODO программа для сжатия изображений
from PIL import Image
import os

ALLOWED_EXTENSIONS = "jpg jpeg png"
QUALITY = 30

image_path = input("Введите путь к изображению: ")

file_name = os.path.basename(image_path)

extension = file_name.split(".")[-1]

if extension not in ALLOWED_EXTENSIONS:
    print("Недопустимый формат файла. Поддерживаемые форматы: jpg, jpeg, png.")
else:
    image = Image.open(image_path)
    new_file_name = file_name.rstrip(f".{extension}") + "_compressed" + ".webp"
    image.save(new_file_name, format="webp", quality=QUALITY)