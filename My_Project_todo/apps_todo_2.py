import os
import json
import datetime


class ToDo:
    def __init__(self, id, title, discription, category="Общее", created_date=None, deadline=None, status=False):
        self.id = id
        self.title = title
        self.discription = discription
        self.category = category
        self.created_date = created_date if created_date else datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        self.deadline = deadline
        self.status = status

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "discription": self.discription,
            "category": self.category,
            "created_date": self.created_date,
            "deadline": self.deadline,
            "status": self.status
        }
    
def load_tasks():
    if os.path.exists("todo_fils.json"):
        with open("todo_fils.json", "r", encoding="utf-8") as file:
            todo_data = json.load(file)
            todos = [ToDo(todo["id"], 
            todo["title"],
            todo["discription"],
            todo["category"],
            todo["created_date"],
            todo["deadline"], 
            todo["status"]) 
            for todo in todo_data]

            return todos
    return []
# Функция сохранения задач
def save_tasks(todos):
    with open("todo_fils.json", "w", encoding="utf-8") as file:
        todo_data = [todo.to_dict() for todo in todos]
        json.dump(todo_data, file, indent=4, ensure_ascii=False)

# Функция добавления задачи!
def add_tasks(todos):
    title = input("Введите название задачи: ")
    discription = input("Введите описание задачи: ")
    category = choose_category()
    deadline = set_deadline()
    

    if todos:
        max_id = max(todo.id for todo in todos) + 1
    else:
        max_id = 1

    new_todo = ToDo(max_id, title, discription, category, None, deadline, False)
    todos.append(new_todo)
    save_tasks(todos)
    print("Задача успешно добавлена!")

# Функция категории задачи!
def choose_category():
    categories = ["Работа", "Учеба", "Дом", "Личное", "Общее"]
    print("Выберите категорию:")

    for i, category in enumerate(categories, start=1):
        print(f"{i}. {category}")

    try:
        category_index = int(input("Введите номер категории от 1 до 5: ")) - 1

        if 0 <= category_index < len(categories):
            return categories[category_index]
        else:
            print("Неверный выбор категории. Используется категория 'Общее'.")
            return "Общее"

    except ValueError:
        print("Пожалуйста введите число от 1 до 4!")
        return "Общее"
        

# Функция связанная со временем дедлайн
def set_deadline():
    deadline_input = input("Установить дедлайн? (да/нет): ").strip().lower()

    if deadline_input == "да":
        deadline_str = input("Введите дедлайн в формате ГГГГ-ММ-ДД ЧЧ:ММ ")
        try:
            deadline = datetime.datetime.strptime(deadline_str, "%Y-%m-%d %H:%M")
            return deadline.strftime("%Y-%m-%d %H:%M")
        except ValueError:
            print("Неверный формат даты. Дедлайн не установлен.")
    return None

# функция показывает саму задачу!
def show_tasks(todos):
    if not todos:
        print("Список задач пуст!")
        return

    print("\nСписок задач:\n")

    for todo in todos:
        status = "Выполнено" if todo.status else "Не выполнено"
        print(f"{todo.id}. {todo.title} - {status}")
        print(f"Категория: {todo.category}")
        print(f"Создана: {todo.created_date}")
        if todo.deadline:
            print(f"    Дедлайн: {todo.deadline}")
        
        if todo.discription:
            print(f"    Описание: {todo.discription}")
            print()

# Функция редактирование задач
def edit_task(todos):
    show_tasks(todos)
    if not todos:
        return

    try:
        task_id = int(input("Введите ID задачи для редактирования: "))

        for todo in todos:
            if todo.id == task_id:
                print("\nЧто хотите изменить?")
                print("1. Название")
                print("2. Описание")
                print("3. Категорию")
                print("4. Дедлайн")
                print("5. Отмена")

                choice = input("Выберите вариант (1-5): ")

                if choice == "1":
                    new_title = input("Введите новое название задачи: ")
                    todo.title = new_title
                elif choice == "2":
                    new_discription = input("Введите новое описание задачи: ")
                    todo.discription = new_discription
                elif choice == "3":
                    todo.category = choose_category()
                elif choice == "4":
                    todo.deadline = set_deadline()
                elif choice == "5":
                    print("Редактирование отменено.")
                save_tasks(todos)
                print("Задача успешно отредактирована!")
                return
            else:
                print(f"Задача с ID {task_id} не найдена.")
    except ValueError:
        print("Пожалуйста, введите число")
        

# функция меняет статус задачи!
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
        print(f"Задача с ID {task_id} не найдена.")

    except ValueError:
        print("Пожалуйста введите число!!!")

# Функция просроченой задачи
def show_overdue_tasks(todos):
    current_time = datetime.datetime.now()
    overdue_tasks = []

    for todo in todos:
        if not todo.status and todo.deadline:
            try:
                deadline_time = datetime.datetime.strptime(todo.deadline, "%Y-%m-%d %H:%M")
                if deadline_time < current_time:
                    overdue_tasks.append(todo)
            except ValueError:
                continue
    
    if overdue_tasks:
        print("\nПросроченные задачи:")
        show_tasks(overdue_tasks)
    else:
        print("Нет просроченных задач!")
            
# Функция поиска по ключевым словам
def search_tasks(todos):
    keyword = input("Введите ключевое слово для поиска: ").lower()
    found_tasks = []

    for todo in todos:
        if keyword in todo.title.lower() or (todo.discription and keyword in todo.discription.lower()):
            found_tasks.append(todo)

    if found_tasks:
        print("\nНайденые задачи из поиска")
        show_tasks(found_tasks)
    else:
        print("\nЗадачи не найдены!")

# Функция поиска по статусу задач
def filter_by_status(todos):
    if not todos:
        print("Список задач пуст!")
        return
    
    print("\nФильтр по статусу:\n")
    print("1. Все задачи")
    print("2. Только выполненные")
    print("3. Только невыполненные\n")
    
    choice = input("Выберите вариант (1-3): ")
    
    filtered_tasks = []
    if choice == "1":
        filtered_tasks = todos
    elif choice == "2":
        filtered_tasks = [todo for todo in todos if todo.status]
    elif choice == "3":
        filtered_tasks = [todo for todo in todos if not todo.status]
    else:
        print("Неверный выбор!")
        return
    
    if filtered_tasks:
        show_tasks(filtered_tasks)
    else:
        print("Задачи не найдены!")

# функция поиска по категория 
def filter_by_category(todos):
    if not todos:
        print("\nСписок задач пуст!")
        return
    print("Выберите категории\n")
    categories = ["Работа", "Учеба", "Дом", "Личное", "Общее"]

    for i, category in enumerate(categories, start=1):
        print(f"{i}. {category}\n")

    try:
        category_index = int(input("Введите номер категории от 1 до 5: ")) - 1

        if 0 <= category_index < len(categories):
            filtered_tasks = [todo for todo in todos if todo.category == categories[category_index]]

            if filtered_tasks:
                show_tasks(filtered_tasks)
            else:
                print(f"В категории {categories[category_index]} нет задач!")
        else:
            print("Неверный выбор категории!")
    except ValueError:
        print("Пожалуйста введите число от 1 до 5!")

# Функция статистики задач
def show_statistics(todos):
    total_tasks = len(todos)
    total_tasks_status_ok = sum(1 for todo in todos if todo.status)
    total_tasks_status_not_ok = total_tasks - total_tasks_status_ok
    percentage_completed = (total_tasks_status_ok / total_tasks) * 100 if total_tasks > 0 else 0

    category_count = {}

    for todo in todos:
        category_count[todo.category] = category_count.get(todo.category, 0) + 1

    print("\nСтатистика задач:")

    print(f"Общее количество задач: {total_tasks}")
    print(f"Выполненные задачи: {total_tasks_status_ok}")
    print(f"Невыполненные задачи: {total_tasks_status_not_ok}")
    print(f"Процент выполненных задач: {percentage_completed:.2f}%")

    print("\nКоличество задач по категориям:")

    for category, count in category_count.items():

        print(f"{category}: {count}")

# Функция экспорта в .txt файл
def export_tasks(todos):
    with open("tasks_report.txt", "w", encoding="utf-8") as file:
        file.write("Отчет по задачам\n")
        file.write(f"Дата генерации: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        file.write("\nСписок задач:\n")

        for todo in todos:
            status = "Выполнено" if todo.status else "Не выполнено"
            file.write(f"\nЗадача #{todo.id}\n")
            file.write(f"{todo.id}. {todo.title} - {status}\n")
            file.write(f"Категория: {todo.category}\n")
            file.write(f"Статус: {status}\n")
            file.write(f"Создана: {todo.created_date}\n")
            if todo.deadline:
                file.write(f"Дедлайн: {todo.deadline}\n")

            if todo.discription:
                file.write(f"Описание: {todo.discription}\n")
        
        file.write(f"\nВсего задач: {len(todos)}")
        print("Отчет успешно экспортирован в файл tasks_report.txt")


# функция удаления задач
def delete_tasks(todos):
    show_tasks(todos)
    if not todos:
        return
    
    try:
        task_id = int(input(f"Введите ID задачи, чтобы удалить её: "))

        for i, todo in enumerate(todos):
            if todo.id == task_id:
                delete_todo = todos.pop(i)
                save_tasks(todos)
                print(f"Задача с id {task_id} удалена")
                return
            
        print(f"Задача с ID {task_id} не найдена.")

    except ValueError:
        print("Пожалуйста введите число!!!")


# Финальаня функция для запуска
def main():
    todos = load_tasks()

    while True:
        print("\n========================")
        print("\nTODO приложение:\n")
        print("1. Добавить задачу")
        print("2. Показать все задачи")
        print("3. Изменить статус задачи")
        print("4. Удалить задачу")
        print("5. Показать просроченные задачи")
        print("6. Поиск по ключевым словам!")
        print("7. Фильтрация по статусу")
        print("8. Фильтрация по категории")
        print("9. Редактировать задачу")
        print("10. Статистика и отчеты")
        print("11. Экспорт файла задач")
        print("12. Выйти из приложения!\n")

        choice = input(f"Выберите действие: (1-12): ")
        print("\n========================")

        if choice == "1":
            add_tasks(todos)
        elif choice == "2":
            show_tasks(todos)
        elif choice == "3":
            toggle_task_status(todos)
        elif choice == "4":
            delete_tasks(todos)
        elif choice == "5":
            show_overdue_tasks(todos)
        elif choice == "6":
            search_tasks(todos)
        elif choice == "7":
            filter_by_status(todos)
        elif choice == "8":
            filter_by_category(todos)
        elif choice == "9":
            edit_task(todos)
        elif choice == "10":
            show_statistics(todos)
        elif choice == "11":
            export_tasks(todos)
        elif choice == "12":
            print("Вы вышли из приложения!")
            break
        else:
            print("Неверный выбор! Выберите число от 1 до 12!!!")


# функция заупска
if __name__ == "__main__":
    main()
