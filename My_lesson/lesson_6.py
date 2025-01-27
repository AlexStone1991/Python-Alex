# TODO Циклы. Операторы упралвения циклами. Работа со списками. Урок 6

# names = ["Басков", "Киркоров", "Бузовы", "Пугачева"]

# no_r_names = []

# for name in names:
#     # Посчитаем буквы р если 2 и более - выходим из цикла
#     if name.lower().count("р") > 1:
#         print("Слишком много букв р")
#         break
    
#     if "р" in name.lower(): # or "r" in name.lower(): - если англ буква!
#         continue
    


#     no_r_names.append(name)

# print(no_r_names)

# задача - перепишите это так чтобы испольовался continue на фамилиях где больше 6 символов остальные добавляются в список sorted_names

# names = ["Басков", "Киркоров", "Бузова", "Пугачева", "Макарова", "Макаровна", "Майкл Джексон", "Фейс", "Джарахов", "Монеточка"]
# sorted_names = []

# for name in names:
#     if len(name) > 6:
#         continue
#     sorted_names.append(name)

# print(sorted_names)

# # короткий вариант! верхнего кода!
# short_names = [name for name in names if len(name) <= 6]
# print(short_names)

# potates = ["картошка", "картошка", "картошка", "гниль", "гниль", "картошка", "гниль", "картошка"]

# POTATES_NEEDED = 4

# potates_count = 0

# potates_plate = []

# for potate in potates:
#     if potates_count >= POTATES_NEEDED:
#         break
    
#     if potate == "гниль":
#         print("Сорри, но это гниль")
#         continue

#     #чистим картоху
#     potate += "_чищенная"
#     potates_plate.append(potate)
#     potates_count += 1
# # блок отрабатывает если цикл не был прерван break
# else:
#     print(f"Картошки не хватило\nПочищено {potates_count} картошек из {POTATES_NEEDED}")

# print(potates_plate)

# # короткий вариант! верхнего кода с картошккой!
# potates_plate = [potate + "_чищенная" for potate in potates if potate != "гниль"]
# print(potates_plate)

# Range - Послеедовательность чисел



# WHILE - цикл с предусловием



# elemet_count = 0

# while True:
#     elemet_count += 1
#     print(f"в {elemet_count} раз, купи выпить!")
#     if elemet_count >= 5:
#         break

# while  elemet_count < 5:
#     elemet_count += 1
#     print(f"в {elemet_count}й раз, купи выпить!")

# практика программа купи айфон

# обьявите цикл while true
# внутри цикла сделайте print("Купи айфон")
# Пользовательский ввод для ответа
# если ответ == "куплю", радумаем и выходим из цикла break
# иначе форматированная строка, все говорят {user_input} а ты купи айфон

# while True:
#     print("Купи айфон")
#     user_input = input("Купишь? ")
#     if user_input == "куплю":
#         print("Отлично, купил!")
#         break
#     else:
        # print(f"Все говорят {user_input}, а ты купи айфон")

# START_NUM = 0
# END_NUM = 6
# STEP = 1

# my_range = [] # [1, 2, 3, 4, 5]

# while START_NUM < END_NUM:
#     my_range.append(START_NUM)
#     START_NUM += STEP
# print(my_range)

# START_NUM = 0
# END_NUM = 6
# STEP = 1

# my_range = range(START_NUM, END_NUM, STEP)
# print(list(my_range))
# print(my_range)
# print(type(my_range))

# potates = ["картошка", "картошка", "картошка", "гниль", "гниль", "картошка", "гниль", "картошка"]

# # for i in range(100):
# #     print(f"Индекс {i}")
# #     print(potates[i])
# # получаем кол-во итераций равное длине списка
# for i in range(len(potates)):
#     print(f"Индекс {i}")

#     potate = potates[i]
# # как получить индексы этого элемента?
# # подстава мы получаем первый элемент и его индекс
# # картошка всего 0 а гниль всегда 3
#     print(potates.index(potate))


# работа с ord и chr
# ord - возвращает числовой код символа
# chr - возвращает символ по числовому коду
food = "шаурма для кота"
STPEP = -1

encode_string = []

for letter in food:
    encode_letter = ord(letter)
    encode_string.append(encode_letter)

print(encode_string)

[print(chr(letter), end="") for letter in encode_string]

russians_letters = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
print(russians_letters)
for i in range(0, 50):
    print(chr(i)) 

# import os
# # oslistdir() - возвращает список файлов и директории в текущей директоии

# dir_path = r"C:\\Users\\ALEXSTONE\\Documents\\2"
# files = os.listdir(dir_path)

# print(f"файлы папки {dir_path}:")
# for file in files:
#     print(file)

# # проверка папки или файла os.path.isdir() os.path.isfile()
# # os.path.join() - соединяет пути к файлу и название файла

# for file in files:
#     full_path = os.path.join(dir_path, file)
#     print(full_path)

#     if os.path.isdir(full_path):
#         print(f"{file} - это директория")
#     elif os.path.isfile(full_path):
#         print(f"{file} - это файл")
#     else:
#         print(f"{file} - это что-то еще")

# какая то не понятная ошибка и программа не пашет! ну и вроде как не нужна 