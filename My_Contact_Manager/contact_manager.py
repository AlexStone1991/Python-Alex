# Хранение контактов: имя, телефон, email, группа
# Поиск контактов по имени/телефону
# Группировка по категориям (друзья, работа, семья)
# Импорт/экспорт контактов

"""
КРУТЫЕ ФИЧИ:
📞 Умный поиск по части имени/телефона
📂 Группы контактов
📊 Статистика по группам
💾 Резервное копирование
🔍 Быстрый поиск
"""

from datetime import datetime
import os
import json

class Contact():
    FRIENDS = "друзья"
    WORK = "работа"
    FAMILY = "семья"
    OTHER = "другое"
    
    def __init__(self, id, name, phone, email="", group=OTHER, notes="", date=None):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email
        self.group = group
        self.notes = notes
        self.date = date if date else datetime.now().strftime("%d.%m.%Y %H:%M")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "group": self.group,
            "notes": self.notes,
            "date": self.date
        }
    
def add_contact(contacts):

    id = len(contacts) + 1
    name = input("Введите имя контакта: ")
    phone = input("Введите номер телефона: ")
    email = input("Введите email (если есть): ")
    group = input("Введите группу (друзья, работа, семья, другое): ").lower()
    notes = input("Введите заметки (если есть): ")
    contact = Contact(id, name, phone, email, group, notes)
    contacts.append(contact)
    print(f"Контакт {name} добавлен!")

def save_contacts(contacts):
    with open("contacts.json", "w", encoding="utf-8") as file:
        json.dump([contact.to_dict() for contact in contacts], file, ensure_ascii=False, indent=4)

def load_contacts():
    if os.path.exists("contacts.json"):
        with open("contacts.json", "r", encoding="utf-8") as file:
            contacts_data = json.load(file)
            contacts = []
            for contact_data in contacts_data:
                contacts.append(Contact(**contact_data))
            return contacts
    else:
        return []
        

# поиск по имени/телефону
def search_contacts(contacts):
    search_term = input("Введите имя или телефон для поиска: ").lower()
    found_contacts = []
    
    for contact in contacts:
        if search_term in contact.name.lower() or search_term in contact.phone:
            found_contacts.append(contact)

    if found_contacts:
        print("\nНайденные контакты:")
        for contact in found_contacts:
            print(f"{contact.id}. {contact.name} - {contact.phone} ({contact.group})")

        try:
            contact_id = int(input("Введите ID контакта для просмотра (или 0 для выхода): "))
            
            if contact_id == 0:
                return
                
            # Ищем контакт по REAL ID, а не индексу в found_contacts
            selected_contact = None
            for contact in found_contacts:
                if contact.id == contact_id:
                    selected_contact = contact
                    break
            
            if selected_contact:
                print(f"\nИнформация о контакте {selected_contact.name}:")
                print(f"Телефон: {selected_contact.phone}")
                print(f"Email: {selected_contact.email}")
                print(f"Группа: {selected_contact.group}")
                print(f"Заметки: {selected_contact.notes}")
            else:
                print("Контакт с таким ID не найден в результатах поиска.")
                
        except ValueError:
            print("Пожалуйста, введите число!")
    else:
        print("Контакты не найдены.")

# def show_all_contacts(contacts):
def show_all_contacts(contacts):
    if not contacts:
        print("Список контактов пуст.")

    print("\nСписок всех контактов:")

    for contact in contacts:
        print(f"\nID {contact.id}")
        print(f"Имя: {contact.name}")
        print(f"Телефон: {contact.phone}")
        print(f"Email: {contact.email}")
        print(f"Группа: {contact.group}")
        print(f"Заметки: {contact.notes}")
        print(f"Дата добавления: {contact.date}")
        print("-" * 30)

def edit_contact(contacts):
    if not contacts:
        print("Список контактов пуст.")
        return

    # Показываем все контакты для выбора
    show_all_contacts(contacts)
    
    try:
        contact_id = int(input("\nВведите ID контакта для редактирования: "))
        
        # Ищем контакт по ID
        for contact in contacts:
            if contact.id == contact_id:
                print(f"\nРедактирование контакта: {contact.name}")
                
                # Предлагаем изменить каждое поле
                new_name = input(f"Имя ({contact.name}): ") or contact.name
                new_phone = input(f"Телефон ({contact.phone}): ") or contact.phone
                new_email = input(f"Email ({contact.email}): ") or contact.email
                new_group = input(f"Группа ({contact.group}): ") or contact.group
                new_notes = input(f"Заметки ({contact.notes}): ") or contact.notes
                
                # Обновляем контакт
                contact.name = new_name
                contact.phone = new_phone
                contact.email = new_email
                contact.group = new_group
                contact.notes = new_notes
                
                print("Контакт успешно обновлен!")
                return
                
        print("Контакт с таким ID не найден.")
        
    except ValueError:
        print("Пожалуйста, введите число!")

def delete_contact(contacts):
    if not contacts:
        print("Список контактов пуст.")
        return

    # Показываем все контакты
    show_all_contacts(contacts)
    
    try:
        contact_id = int(input("\nВведите ID контакта для удаления: "))
        
        # Ищем контакт по ID
        for i, contact in enumerate(contacts):
            if contact.id == contact_id:
                # Подтверждение удаления
                confirm = input(f"Удалить контакт '{contact.name}'? (да/нет): ")
                if confirm.lower() == 'да':
                    deleted_contact = contacts.pop(i)
                    print(f"Контакт '{deleted_contact.name}' удален!")
                    return
                else:
                    print("Удаление отменено.")
                    return
                    
        print("Контакт с таким ID не найден.")
        
    except ValueError:
        print("Пожалуйста, введите число!")

def main():
    contacts =  load_contacts()
    
    while True:
        print("\n=== КОНТАКТНЫЙ МЕНЕДЖЕР ===")
        print("1. Добавить контакт")
        print("2. Показать все контакты") 
        print("3. Найти контакт")
        print("4. Редактировать контакт")
        print("5. Удалить контакт")
        print("6. Выйти")
        
        choice = input("Выберите действие: ")
        
        if choice == "1":
            add_contact(contacts)
            save_contacts(contacts)
        elif choice == "2":
            show_all_contacts(contacts)
        elif choice == "3":
            search_contacts(contacts)
        elif choice == "4":
            edit_contact(contacts)
            save_contacts(contacts)
        elif choice == "5":
            delete_contact(contacts)
            save_contacts(contacts)
        elif choice == "6":
            break
        else:
            print("Неверный выбор!")

if __name__ == "__main__":
    main()

        



