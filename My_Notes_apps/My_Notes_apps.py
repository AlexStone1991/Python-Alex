# Приложение Notes
import os
import json
from datetime import datetime

class Notes:
    def __init__(self, id, title, text, category="Общие", date=None):
        self.id = id
        self.title = title
        self.text = text
        self.category = category
        self.date = date if date else datetime.now().strftime("%Y-%m-%d %H:%M")

    def to_dict(self):
        return{
        "id": self.id,
        "title": self.title,
        "text": self.text,
        "category": self.category,
        "date": self.date
    }


def load_notes():
    if os.path.exists("notes.json"):
        with open("notes.json", "r", encoding="utf-8") as file:
            notes_data = json.load(file)

            notes = [Notes(note["id"],
            note["title"],
            note["text"],
            note["category"],
            note["date"])
            for note in notes_data]

            return notes
    return []


def save_notes(notes):
    with open("notes.json", "w", encoding="utf-8") as file:
        notes_data = [note.to_dict() for note in notes]
        json.dump(notes_data, file, indent=4, ensure_ascii=False)

def add_notes(notes):
    title = input("Введите название заметки: ")
    text = input("Введите текст заметки: ")
    category = choose_category()

    if notes:
        max_id = max(note.id for note in notes) + 1

    else:
        max_id = 1

    new_note = Notes(max_id, title, text, category, None)

    notes.append(new_note)

    save_notes(notes)
    print(f"Заметка успешно добавлена!")


def choose_category():
    categories = ["Работа", "Учеба", "Дом", "Личное", "Общие"]

    for i, category in enumerate(categories, start=1):
        print(f"{i}. {category}")

    try:
        category_index = int(input("Введите номер категории от 1 до 5: ")) - 1

        if 0 <= category_index < len(categories):
            return categories[category_index]
        else:
            print("Неверный выбор категории. Используется категория 'Общие'.")
    except ValueError:
        print("Пожалуйста введите число от 1 до 5!")

def show_all_notes(notes):
    if not notes:
        print("Список заметок пуст!")
        return
    print("\nСписок заметок:\n")

    for note in notes:
        print(f"{note.id}. {note.title}")
        print(f"Текст: {note.text}")
        print(f"Категория: {note.category}")
        print(f"Дата создания: {note.date}")

def edit_notes(notes):
    show_all_notes(notes)
    if not notes:
        print("Список пуст")
        return
    try:
        note_id = int(input("Введите ID заметки для редактирования: "))
        for note in notes:
            if note.id == note_id:
                print("\nЧто хотите изменить?")
                print("1. Название")
                print("2. Текст")
                print("3. Категорию")

                choice = input("Выберите вариант (1-3): ")

                if choice == "1":
                    new_title = input("Введите новое название заметки: ")
                    note.title = new_title

                elif choice == "2":
                    new_text = input("Введите новый текст заметки: ")
                    note.text = new_text

                elif choice == "3":
                    note.category = choose_category()

                save_notes(notes)
                print("Заметка успешно отредактирована!")

    except ValueError:
        print("Пожалуйста введите число!")

def delete_notes(notes):
    show_all_notes(notes)
    if not notes:
        print("Список заметок пуст!")
        return
    
    try:

        note_id = int(input("Введите ID заметки для удаления: "))

        for i, note in enumerate(notes):

            if note.id == note_id:

                delete_note = notes.pop(i)

                save_notes(notes)
                print(f"Заметка с id {note_id} удалена!")

    except ValueError:
        print("Пожалуйста введите число!")

def main():
    notes = load_notes()

    while True:
        print("\n========================")
        print("\nПриложение заметки:\n")

        print("1. Добавить заметку")
        print("2. Показать все заметки")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выйти из приложения")

        choice = input("Выберите действие: (1-5): ")
        if choice == "1":
            add_notes(notes)
        elif choice == "2":
            show_all_notes(notes)
        elif choice == "3":
            edit_notes(notes)
        elif choice == "4":
            delete_notes(notes)
        elif choice == "5":
            print("Вы вышли из приложения!")
            break
        else:
            print("Неверный выбор! Выберите число от 1 до 5!")

if __name__ == "__main__":
    main()

