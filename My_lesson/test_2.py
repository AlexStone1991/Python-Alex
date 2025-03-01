import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Камень, ножницы, бумага")

        self.choices = ['камень', 'ножницы', 'бумага']
        self.user_choice = tk.StringVar()
        self.result_text = tk.StringVar()

        tk.Label(root, text="Выберите ваш ход:").pack()

        for choice in self.choices:
            tk.Radiobutton(root, text=choice, variable=self.user_choice, value=choice).pack(anchor="w")

        tk.Button(root, text="Играть", command=self.play_game).pack()

        self.result_label = tk.Label(root, textvariable=self.result_text, font=("Helvetica", 14))
        self.result_label.pack()

    def play_game(self):
        user_choice = self.user_choice.get()
        if not user_choice:
            messagebox.showwarning("Предупреждение", "Пожалуйста, выберите ваш ход.")
            return

        computer_choice = random.choice(self.choices)
        result = self.determine_winner(user_choice, computer_choice)

        self.result_text.set(f"Вы выбрали: {user_choice}\nКомпьютер выбрал: {computer_choice}\n{result}")

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "Ничья!"
        elif (user_choice == 'камень' and computer_choice == 'ножницы') or \
             (user_choice == 'ножницы' and computer_choice == 'бумага') or \
             (user_choice == 'бумага' and computer_choice == 'камень'):
            return "Вы выиграли!"
        else:
            return "Компьютер выиграл!"

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
