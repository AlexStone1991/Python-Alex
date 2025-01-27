# user = str(input("Выберите: камень, ножницы, бумага: "))

# for kamen in user:
#     if kamen == "камень":
#         print("ИИ выбрал камень - ничья")
#     elif kamen == "ножницы":
#         print("ИИ выбрал ножницы - выиграл")
#     elif kamen == "бумага":
#         print("ИИ выбрал бумага - выиграл")

n = int(input("Введите длинну строки: "))

user_list = []

i = 0
while i < n:
    vvod = "Введите элемент списка #" + str(i + 1) + ": "
    user_list.append(input(vvod))
    i += 1
print(user_list)