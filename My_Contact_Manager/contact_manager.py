from datetime import datetime
import os
import json
from colorama import Fore, Back, Style, init
init(autoreset=True)

# print(Fore.RED + "Это красный текст")
# print(Fore.GREEN + "Это зеленый текст") 
# print(Fore.YELLOW + "Это желтый текст")
# print(Fore.CYAN + "Это бирюзовый текст")
# print(Style.BRIGHT + "Это яркий текст")

class Contact():
    FRIENDS = "друзья"
    WORK = "работа"
    FAMILY = "семья"
    OTHER = "другое"
    
    def __init__(self, id, name, phone, email="", group=OTHER, notes="", date=None):
        self.id = id
        self.name = name
        self.phone = phone.replace(" ", "").replace("(", "").replace(")", "").replace("-", "")
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

# Добавление контакта
def add_contact(contacts):

    id = len(contacts) + 1
    name = input("Введите имя контакта: ")
    while True:
        phone = input("Введите номер телефона: ")
        is_valid = validate_phone(phone)
        if is_valid:
            break
        else:
            print(f"{Fore.RED}Неверный формат номера телефона. Попробуйте снова.")

    while True:
        email = input("Введите email (если есть): ")
        if validate_email(email):
            break
        else:
            print(f"{Fore.RED}Неверный формат email. Попробуйте снова.")
    while True:
        group = input("Введите группу (друзья, работа, семья, другое): ").lower()
        if validate_group(group):
            break
        else:
            print(f"{Fore.RED}Попробуйте снова.")
    notes = input("Введите заметки (если есть): ")
    contact = Contact(id, name, phone, email, group, notes)
    contacts.append(contact)
    print(f"{Fore.GREEN}Контакт {name} добавлен!")

# Сохранение и загрузка контактов
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

# Валидация телефона
def validate_phone(phone):
    if not phone:
        print(f"{Fore.RED}Номер телефона не может быть пустым.")
        return False

    cleaned_phone = phone.replace(" ", "").replace("(", "").replace(")", "").replace("-", "")
    if not cleaned_phone.isdigit():
        print(f"{Fore.RED}Номер телефона должен содержать только цифры.")
        return False
    
    if len(cleaned_phone) < 5 or len(cleaned_phone) > 11:
        print(f"{Fore.RED}Номер телефона должен содержать не менее 5 и не больше 11 цифр.")
        return False
    return True

# Валидация email
def validate_email(email):
    if not email:
        return True
    if "@" not in email:
        print(f"{Fore.RED}Email должен содержать символ @")
        return False
    parts = email.split("@")

    if len(parts) !=2:
        print(f"{Fore.RED}Неверный формат email")
        return False
    
    if "." not in parts[1]:
        print(f"{Fore.RED}Должна быть точка после @")
        return False
    
    domin_parts = parts[1].split(".")
    
    if len(domin_parts[-1]) < 2:
        print(f"{Fore.RED}После точки должен быть домен (ru, com и т.д.)")
        return False
    return True

def validate_group(group):
    valid_groups = [Contact.FRIENDS, Contact.WORK, Contact.FAMILY, Contact.OTHER]
    if group in valid_groups:
        return True
    else:
        print(f"{Fore.RED}Неверная группа. Выберите из: друзья, работа, семья, другое")
        return False

# Статистика по группам
def show_contact_stats(contacts):
    if not contacts:
        print(f"{Fore.RED}Список контактов пуст.")
        return

    group_counts = {}
    
    for contact in contacts:
        if contact.group in group_counts:
            group_counts[contact.group] += 1
        else:
            group_counts[contact.group] = 1

    print("\nСТАТИСТИКА ПО ГРУППАМ")
    for group, count in group_counts.items():
        print(f"{Fore.BLUE}{group.capitalize()}: {count} контактов")
    most_popular_group = max(group_counts, key=group_counts.get)
    print(f"\n{Fore.GREEN}Самая популярная группа: {most_popular_group.capitalize()}")

# поиск по имени/телефону
def search_contacts(contacts):
    search_term = input("Введите имя или телефон для поиска: ").lower()
    found_contacts = []
    
    for contact in contacts:
        if search_term in contact.name.lower() or search_term in contact.phone:
            found_contacts.append(contact)

    if found_contacts:
        print(f"\n{Fore.BLUE}Найденные контакты:")
        for contact in found_contacts:
            print(f"{Fore.GREEN}{contact.id}. {contact.name} - {contact.phone} ({contact.group})")

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
                print(f"\n{Fore.GREEN}Информация о контакте {selected_contact.name}:")
                print(f"{Fore.YELLOW}Телефон: {selected_contact.phone}")
                print(f"{Fore.BLUE}Email: {selected_contact.email}")
                print(f"{Fore.BLUE}Группа: {selected_contact.group}")
                print(f"{Fore.BLUE}Заметки: {selected_contact.notes}")
            else:
                print(f"{Fore.RED}Контакт с таким ID не найден в результатах поиска.")
                
        except ValueError:
            print(f"{Fore.RED}Пожалуйста, введите число!")
    else:
        print(f"{Fore.RED}Контакты не найдены.")

# показать все контакты
def show_all_contacts(contacts):
    if not contacts:
        print(f"{Fore.RED}Список контактов пуст.")

    print(f"\n{Fore.BLUE}Список всех контактов:")

    for contact in contacts:
        print(f"\n{Fore.YELLOW}ID {Style.BRIGHT}{contact.id}")
        print(f"{Fore.GREEN}Имя: {Style.BRIGHT}{contact.name}")
        print(f"{Fore.BLUE}Телефон: {contact.phone}")
        print(f"{Fore.BLUE}Email: {contact.email}")
        print(f"{Fore.BLUE}Группа: {contact.group}")
        print(f"{Fore.BLUE}Заметки: {contact.notes}")
        print(f"{Fore.YELLOW}Дата добавления: {Style.BRIGHT}{contact.date}")
        print("-" * 30)

# редактирование контакта
def edit_contact(contacts):
    if not contacts:
        print(f"{Fore.RED}Список контактов пуст.")
        return

    # Показываем все контакты для выбора
    show_all_contacts(contacts)
    
    try:
        contact_id = int(input("\nВведите ID контакта для редактирования: "))
        
        # Ищем контакт по ID
        for contact in contacts:
            if contact.id == contact_id:
                print(f"\n{Fore.BLUE}Редактирование контакта: {contact.name}")
                
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
                
                print(f"{Fore.GREEN}Контакт успешно обновлен!")
                return
                
        print(f"{Fore.RED}Контакт с таким ID не найден.")
        
    except ValueError:
        print(f"{Fore.RED}Пожалуйста, введите число!")

# удаление контакта
def delete_contact(contacts):
    if not contacts:
        print(f"{Fore.RED}Список контактов пуст.")
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
                    print(f"{Fore.GREEN}Контакт '{deleted_contact.name}' удален!")
                    return
                else:
                    print(f"{Fore.BLUE}Удаление отменено.")
                    return
                    
        print(f"{Fore.RED}Контакт с таким ID не найден.")
        
    except ValueError:
        print(f"{Fore.RED}Пожалуйста, введите число!")

def backup_contacts(contacts):
    backup_dir = "backups"
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = os.path.join(backup_dir, f"contacts_backup_{timestamp}.json")

    with open(backup_file, "w", encoding="utf-8") as file:
        json.dump([contact.to_dict() for contact in contacts], file, ensure_ascii=False, indent=4)
    print(f"{Fore.GREEN}backup создан!")

# главная функция
def main():
    contacts =  load_contacts()
    
    while True:
        print(f"\n{Fore.CYAN}{Style.BRIGHT}=== КОНТАКТНЫЙ МЕНЕДЖЕР ===\n")
        print(f"{Fore.YELLOW}1. Добавить контакт")
        print(f"{Fore.YELLOW}2. Показать все контакты")
        print(f"{Fore.YELLOW}3. Найти контакт")
        print(f"{Fore.YELLOW}4. Редактировать контакт")
        print(f"{Fore.YELLOW}5. Удалить контакт")
        print(f"{Fore.YELLOW}6. Статистика по группам")
        print(f"{Fore.YELLOW}7. Создать резервную копию")
        print(f"{Fore.YELLOW}8. Выйти")
        
        choice = input(f"\n{Fore.WHITE}{Style.BRIGHT}Выберите действие: ")
        
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
            show_contact_stats(contacts)
        elif choice == "7":
            backup_contacts(contacts)
        elif choice == "8":
            break
        else:
            print(f"{Fore.RED}Неверный выбор!")

    print(f"{Fore.RED}Программа завершена!")

# ЗАпуск функция
if __name__ == "__main__":
    main()
