import random

KAMEN = "камень"
NOJNICI = "ножницы"
BOOMAGA = "бумага"

def get_user_choice():
    while True:
        user_input = input("Введите свой выбор (Камень, Ножницы, Бумага) или 'стоп' для выхода: ").strip().lower()
        if user_input in (KAMEN, NOJNICI, BOOMAGA):
            return user_input
        elif user_input == "стоп":
            return None
        else:
            print("Неправильный ввод. Пожалуйста, введите одно из трех вариантов или 'стоп' для выхода.")

def get_computer_choice():
    return random.choice((KAMEN, NOJNICI, BOOMAGA))

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Ничья!"
    elif (user_choice == KAMEN and computer_choice == NOJNICI) or \
         (user_choice == NOJNICI and computer_choice == BOOMAGA) or \
         (user_choice == BOOMAGA and computer_choice == KAMEN):
        return "Вы победили!"
    else:
        return "Победил ИИ!"

def play_game():
    while True:
        user_choice = get_user_choice()
        if user_choice is None:
            print("Игра окончена.")
            break

        computer_choice = get_computer_choice()

        # Используем capitalize() для вывода с большой буквы
        print(f"Вы выбрали: {user_choice.capitalize()}")
        print(f"Компьютер выбрал: {computer_choice.capitalize()}")
        print(determine_winner(user_choice, computer_choice))
        print()  # Пустая строка для разделения раундов

play_game()
