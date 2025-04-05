# Игра "Угадай число"
import random

class GuessTheNumber:
    def __init__(self, lower_bound=1, upper_bound=50):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.number_to_guess = random.randint(lower_bound, upper_bound)
        self.attempts = 0

    def play(self):
        print(f"Угадайте число от {self.lower_bound} до {self.upper_bound}!")

        while True:
            try:
                guess = int(input("Введите ваше предположение: "))
                self.attempts += 1

                if guess < self.number_to_guess:
                    print("Загаданное число больше.")
                elif guess > self.number_to_guess:
                    print("Загаданное число меньше.")
                else:
                    print(f"Поздравляю! Вы угадали число {self.number_to_guess} за {self.attempts} попыток!")
                    break
            except ValueError:
                print("Пожалуйста, введите целое число.")

# ==========================Запуск игры==========================
# game = GuessTheNumber()
# game.play()




# Игра "Виселица"

import random

class HangmanGame:
    def __init__(self, words):
        self.words = words  # Оставляем слова в исходном формате
        self.word_to_guess = random.choice(self.words)
        self.guessed_letters = set()
        self.attempts_left = 6
        self.current_state = ['_' if letter.islower() else letter for letter in self.word_to_guess]

    def display_hangman(self):
        stages = [  # финальное состояние: полная виселица
            """
               -----
               |   |
               O   |
              /|\  |
              / \  |
                  |
            =========
            """,
            # предыдущие состояния
            """
               -----
               |   |
               O   |
              /|\  |
              /    |
                  |
            =========
            """,
            """
               -----
               |   |
               O   |
              /|\  |
                   |
                  |
            =========
            """,
            """
               -----
               |   |
               O   |
              /|   |
                   |
                  |
            =========
            """,
            """
               -----
               |   |
               O   |
               |   |
                   |
                  |
            =========
            """,
            """
               -----
               |   |
               O   |
                   |
                   |
                  |
            =========
            """,
            """
               -----
               |   |
                   |
                   |
                   |
                  |
            =========
            """
        ]
        return stages[self.attempts_left]

    def update_state(self, guess):
        if guess in self.word_to_guess.lower():
            for i, letter in enumerate(self.word_to_guess):
                if letter.lower() == guess:
                    self.current_state[i] = letter
            return True
        return False

    def get_display_word(self):
        # Возвращает строку с первой буквой в верхнем регистре
        display_word = ''.join(self.current_state)
        return display_word.capitalize()

    def play(self):
        print("Добро пожаловать в игру 'Виселица'!")
        while self.attempts_left > 0 and '_' in self.current_state:
            print(self.display_hangman())
            print("Текущее состояние слова: ", self.get_display_word())
            print(f"Оставшиеся попытки: {self.attempts_left}")
            guess = input("Введите букву: ").lower()  # Приводим ввод к нижнему регистру для проверки

            if guess in self.guessed_letters:
                print("Вы уже предлагали эту букву. Попробуйте другую.")
                continue

            self.guessed_letters.add(guess)

            if self.update_state(guess):
                print("Правильно!")
            else:
                print("Неправильно.")
                self.attempts_left -= 1

        if '_' not in self.current_state:
            print(f"Поздравляю! Вы угадали слово: {self.word_to_guess.capitalize()}")
        else:
            print(f"Вы погибли. Загаданное слово было: {self.word_to_guess.capitalize()}")

# Список слов для игры
words_list = ["яблоко", "банан", "апельсин", "груша", "арбуз", "виноград", "мандарин", "киви", "персик", "слива"]

# ==================================Запуск игры=================================
game = HangmanGame(words_list)
game.play()
