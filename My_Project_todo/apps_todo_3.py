# Пишем приложение ToDo

import os
import json
from datetime import datetime

# 1. Класс Task с: id, title, status
# 2. Добавление задач
# 3. Показ всех задач  
# 4. Изменение статуса
# 5. Удаление задач
# 6. Сохранение в файл

# class Task:
#     def __init__(self, id, title, status=False):
#     def to_dict(self):

# def load_tasks():
# def save_tasks(tasks):

# def add_task(tasks):
# def show_tasks(tasks):
# def toggle_status(tasks):
# def delete_task(tasks):

class ToDo:
    def __init__(self, id, title, status=False):
        self.id = id
        self.title = title
        self.status = status

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "status": self.status
        }
    
def load_tasks():
    if os.path.exists("todo_fils.json"):
        with open("todo_fils.json", "r", encoding="utf-8") as file:
            todo_data = json.load(file)
            todos = [ToDo(todo["id"], todo["title"], todo["status"]) for todo in todo_data]
            return todos 
    return []

def save_tasks(todos):
    with open("todo_fils.json", "w", encoding="utf-8") as file:
        todo_data = [todo.to_dict() for todo in todos]
        json.dump(todo_data, file, indent=4, ensure_ascii=False)

def add_task(todos):
    title = input("Введите название задачи: ")

    if todos:
        max_id = max(todo.id for todo in todos) + 1
    else:
        max_id = 1

    new_todo = ToDo(max_id, title)
    todos.append(new_todo)
    save_tasks(todos)
    print("Задача успешно добавлена!")

def show_tasks(todos):
    if not todos:
        print("Список задач пуст!")

    print("\nСписок задач:\n")

    for todo in todos:
        status = "Выполнено" if todo.status else "Не выполнено"
        print(f"{todo.id}. {todo.title} - {status}")
        print()

def toggle_task_status(todos):
    show_tasks(todos)
    if not todos:
        return
    
    try:
        task_id = int(input("Введите ID задачи, чтобы изменить её статус: "))

        for todo in todos:
            if todo.id == task_id:
                todo.status = not todo.status
                save_tasks(todos)
                print(f"Статус задачи {task_id} изменен")
                return
        print("ЗАДАЧА НЕ НАЙДЕНА!")

    except ValueError:
        print("Пожалуйста введите число!")

def delete_task(todos):
    show_tasks(todos)

    if not todos:
        return
    
    try:
        task_id = int(input("Введите ID задачи, чтобы удалить её: "))

        for i, todo in enumerate(todos):
            if todo.id == task_id:
                delete_todo = todos.pop(i)
                save_tasks(todos)
                print(f"Задача с ID {task_id} удалена!")
                return
        print("ЗАДАЧА НЕ НАЙДЕНА!")
    except ValueError:
        print("Пожалуйста введите число!")

def main():
    todos = load_tasks()

    while True:
        print("\n========================")
        print("\nTODO приложение:")
        print("1. Добавить задачу")
        print("2. Показать все задачи")
        print("3. Изменить статус задачи")
        print("4. Удалить задачу")
        print("5. Выйти")

        choice = input(f"Выберите действие: (1-5): ")
        print("\n========================")
        if choice == "1":
            add_task(todos)
        elif choice == "2":
            show_tasks(todos)
        elif choice == "3":
            toggle_task_status(todos)
        elif choice == "4":
            delete_task(todos)
        elif choice == "5":
            print("Вы вышли из приложения!")
            break
        else:
            print("Неверный выбор. пожалуйста выберите от 1-5.")

if __name__ == "__main__":
    main()