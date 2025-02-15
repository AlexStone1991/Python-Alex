# Хочу написать код игры камень ножницы бумага
import random
KAMEN = "камень"
NOJNICI = "ножницы"
BOOMAGA = "бумага"

def get_user_choice():
    while True:
        user_input = input("Введите свой выбор (Камень, Ножницы, Бумага): ")
        if user_input in (KAMEN, NOJNICI, BOOMAGA):
            return user_input
        else:
            print("Неправильный ввод. Пожалуйста, введите одно из трех вариантов.")
# get_user_choice()
def get_computer_choice():
        return random.choice((KAMEN, NOJNICI, BOOMAGA))

user_choice = get_user_choice()
computer_choice = get_computer_choice()

print(f"Вы выбрали: {user_choice}")
print(f"Компьютер выбрал: {computer_choice}")

if user_choice == computer_choice:
    print("Ничья!")

elif (user_choice == KAMEN and computer_choice == NOJNICI) or (user_choice == NOJNICI and computer_choice == BOOMAGA) or (user_choice == BOOMAGA and computer_choice == KAMEN):
    print("Вы победили!")

elif (computer_choice == KAMEN and user_choice == NOJNICI) or (computer_choice == NOJNICI and user_choice == BOOMAGA) or (computer_choice == BOOMAGA and user_choice == KAMEN):
    print("Победил ИИ!")






