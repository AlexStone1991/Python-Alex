"""
Урок 6
08.12.2023

Завершаем темы из урока 5:
- Операторы break и continue +
- Конструкция for-else +
- Цикл while +
- Основные методы списков -
- Срезы списков +-
- Генерация последовательностей +
- Работа с текстовыми данными

Новые темы урока 6:
- Операторы управления циклом (break, continue, pass) +
- Конструкция for-else +
- Вложенные циклы и их применение
- Шифрование текста:
    - Сдвиг по алфавиту +
    - Работа с ord() и chr() +
- Обход файловой системы через цикл for +
- Валидация паролей:
    - Подсчет различных типов символов
    - Проверка сложности
- Работа с range(): +
    - for i in range()
    - for i in range(len(list))
- Практические задания на все темы

Проекты:
1. Текстовый анализатор
2. Генератор паролей  
3. Шифровальщик текста Цезарь +
4. Камень ножницы бумага !!!
5. Чат с ИИ !!!
"""

# names = ["Басков", "Кирковров", "Бузова", "Пугачева", "Майкл Джексон", "Фейс", "Джарахов", "Монеточка"]

# no_r_names = []

# for name in names:
#      # Посчитаем буквы р если 2 и более - выходим из цикла
#     if name.lower().count("р") > 1:
#         break
    
#     if "р" in name.lower():
#         continue
    
#     no_r_names.append(name)

# print(no_r_names)

#PRACTICE continue
"""
Перепишите это так, чтобы использовался continue на фамилиях где больше 6 символов
Остальные добавлялись в список sorted_names
"""

# short_names = []

# for name in names:
#     if len(name) > 6:
#         continue

#     short_names.append(name)

# short_names = [name for name in names if len(name) <= 6]


# potates = ["картошка", "картошка", "картошка", "гниль", "гниль", "картошка", "гниль", "картошка"]

# POTATES_NEEDED = 3

# potates_count = 0
# potates_plate = []


# for potate in potates:
#     if potates_count >= POTATES_NEEDED:
#         break

#     if potate == "гниль":
#         print(f'{potate} - пропускаем')
#         continue

#     # Чистим картошку
#     potate += "_чищенная"
#     potates_plate.append(potate)
#     potates_count += 1

# # Блок отработает если цикл не был прерван break
# else:
#     print(f'Картошки не хватило\nПочищено {potates_count} картошек из {POTATES_NEEDED}')


# potates_plate = [potate + "_чищенная" for potate in potates if potate != "гниль"]


# print(potates_plate)



# WHILE - цикл с предусловием
elephant_count = 0
# while True:
#     elephant_count += 1
#     print(f'В {elephant_count}й раз, говорю, купи слона')

#     if elephant_count >= 5:
#         break


# while elephant_count < 5:
#     elephant_count += 1
#     print(f'В {elephant_count}й раз, говорю, купи слона')

#PRACTICE Программа "Купи айфон"
"""
1. Объявите цикл while true
2. Внутри цикла сделайте принт "Купи айфон"
3. Пользовательский ввод для ответа
4. Если ответ.lower() == "куплю", радуемся и выходим из цикла break
5. Иначе, форматированная строка. "Все говорят {user_input}, а ты купи айфон"
"""

# 1
# while True:
#     # 2
#     print('Купи айфон')
#     # 3
#     user_input = input('Я жду: ')
#     # 4
#     if user_input.lower() == "куплю":
#         print('Отлично!')
#         break
#     # 5
#     print(f'Все говорят {user_input}, а ты купи айфон')


# Range - последовательность чисел

# START_NUM = 0
# END_NUM = 6
# STEP = 1

# my_range = [] # [0, 1, 2, 3, 4, 5]

# while START_NUM < END_NUM:
#     my_range.append(START_NUM)
#     START_NUM += STEP

# print(my_range)

# range - генератор последовательности чисел
# START_NUM = 0
# END_NUM = 6
# STEP = 1


# my_range = range(START_NUM, END_NUM, STEP)
# print(type(my_range))
# print(my_range)
# print(list(my_range))

# potates = ["картошка", "картошка", "картошка", "гниль", "гниль", "картошка", "гниль", "картошка"]
# ndexError: list index out of range
# for i in range(100):
#     print(f'Индекс {i}')
#     print(potates[i])

# Получаем кол-во итераций раввное длине списка
# for i in range(len(potates)):
#     print(f'Индекс {i}')
#     potato = potates[i]
#     # Как получить индекс этого элемента?
#     # Подстава! Мы молучаем первый элемент и его индекс
#     # картошка всегда 0 а гниль всегда 3
#     print(potates.index(potato))


# Работа с ord() и chr()
# food = "шаурма из кота"
# STPEP = -1
# # ord() - возвращает числовое значение символа
# # chr() - возвращает символ по числовому значению

# encode_string = []

# for letter in food:
#     encode_letter = ord(letter)
#     encode_string.append(encode_letter)

# print(encode_string)

# [print(chr(letter), end="") for letter in encode_string]

russians_letters = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
print(russians_letters)
for i in range(0, 50):
    print(chr(i))

# Обход файловой системы через цикл for
# import os

# # os.listdir() - возвращает список файлов и директорий в текущей директории

# dir_path = r"C:\\Users\\user\\Pictures\\1"
# files = os.listdir(dir_path)

# print(f'Файлы папки {dir_path}:')
# for file in files:
#     print(file)

# # Проверка папка или файл os.path.isdir() os.path.isfile()
# # os.path.join() - объединяет путь к файлу и название файла
# for file in files:
#     full_path = os.path.join(dir_path, file)
#     print(full_path)
    
#     if os.path.isdir(full_path):
#         print(f'{file} - это директория')
#     elif os.path.isfile(full_path):
#         print(f'{file} - это файл')

# # os.path.expanduser(): - расширяет пользовательский путь.


# # Программа сжатия с обходом файловой системы

# from PIL import Image
# import os

# # Допустимые расширения файлов
# ALLOWED_EXTENSIONS = "jpg jpeg png JPEG JPG"
# QUALITY = 40


# image_path = input("Введите путь к изображению или к папке: ").strip().strip('"').strip("'")

# # Проверяем что это. Папка или файл.
# # Если это файл, мы можем быстро конвертировать его в webp
# # Если это папка - мы можем пройтись по всем файлам и конвертировать их

# if not image_path:
#     exit()

# if os.path.isfile(image_path):

#     file_name = os.path.basename(image_path)

#     extension = file_name.split(".")[-1]


#     if extension not in ALLOWED_EXTENSIONS:
#         print("Недопустимое расширение файла")
#     else:
#         image = Image.open(image_path)
#         new_file_name = file_name.rstrip(f".{extension}") + "_compressed" + ".webp"
#         # Формируем путь для сохранения рядом с исходником
#         new_file_path = os.path.join(os.path.dirname(image_path), new_file_name)
#         image.save(new_file_path, format="webp", quality=QUALITY)

# elif os.path.isdir(image_path):
#     # Проходимся по всем файлам в папке
#     for file_name in os.listdir(image_path):
#         full_path = os.path.join(image_path, file_name)
#         if os.path.isfile(full_path):
#             file_name = os.path.basename(full_path)
#             extension = file_name.split(".")[-1]
#             if extension not in ALLOWED_EXTENSIONS:
#                 print(f"Недопустимое расширение файла {file_name}")
#             else:
#                 image = Image.open(full_path)
#                 new_file_name = file_name.rstrip(f".{extension}") + "_compressed" + ".webp"
#                 # Формируем путь для сохранения рядом с исходником
#                 new_file_path = os.path.join(image_path, new_file_name)
#                 image.save(new_file_path, format="webp", quality=QUALITY)


"""
1. append(item) - добавляет элемент item в конец списка
   Обязательные аргументы: item (элемент для добавления)
   
2. extend(iterable) - расширяет список, добавляя элементы из iterable в конец
   Обязательные аргументы: iterable (итерируемый объект)

3. insert(index, item) - вставляет элемент item по указанному индексу index
   Обязательные аргументы: index (позиция для вставки), item (элемент для вставки)

4. remove(item) - удаляет первое вхождение элемента item из списка
   Обязательные аргументы: item (элемент для удаления)

5. pop([index]) - удаляет и возвращает элемент по индексу index
   Опциональные аргументы: index (индекс элемента, по умолчанию -1)

6. clear() - удаляет все элементы из списка
   Без аргументов

7. index(item[, start[, end]]) - возвращает индекс первого вхождения элемента item
   Обязательные аргументы: item (искомый элемент)
   Опциональные аргументы: start (начальный индекс поиска), end (конечный индекс поиска)

8. count(item) - возвращает количество вхождений элемента item в список
   Обязательные аргументы: item (элемент для подсчета)

9. sort(*, key=None, reverse=False) - сортирует список на месте
   Опциональные аргументы: key (функция для определения критерия сортировки), 
                          reverse (порядок сортировки)

10. reverse() - разворачивает список на месте
    Без аргументов

11. copy() - возвращает поверхностную копию списка
    Без аргументов


"""
