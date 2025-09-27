# BUDGET TRACKER приложение!

# Учет доходов и расходов
# Категории трат (еда, транспорт, развлечения)
# Статистика по месяцам/категориям
# Бюджет на месяц

"""
БАЗОВЫЙ ФУНКЦИОНАЛ:
✅ Добавление дохода/расхода
✅ Просмотр всех операций
✅ Статистика по категориям
✅ Баланс на текущий момент
✅ Сохранение в файл
"""
# add_transaction() - добавление операции
# show_balance() - текущий баланс
# show_transactions() - список всех операций
# show_statistics() - статистика по категориям

# Доходы: зарплата, инвестиции, подарки
# Расходы: еда, транспорт, жилье, развлечения

"""
🎯 ПЛАН РАЗРАБОТКИ ПО ДНЯМ:
День 1: Класс Transaction + добавление операций
День 2: Показ операций + баланс
День 3: Статистика по категориям
День 4: Фильтрация по дате/типу
День 5: Бюджет + предупреждения
"""

from datetime import datetime
import os
import json



class Transaction:
    INCOME = "доход"
    EXPENSE = "расход"

    # Категории доходов
    SALARY = "зарплата"
    INVESTMENTS = "инвестиции" 
    GIFTS = "подарки"
    OTHER_INCOME = "другие доходы"
    
    # Категории расходов
    FOOD = "еда"
    TRANSPORT = "транспорт"
    HOUSE = "жилье"
    ENTERTAINMENT = "развлечения"
    OTHER_EXPENSE = "другие расходы"

    def __init__(self, id, type, category, amount, description="", date=None,):
        if type not in (self.INCOME, self.EXPENSE):
            raise ValueError("Неверный тип транзакции. Используйте 'доход' или 'расход'.")
        
        self.id = id
        self.type = type
        self.category = category
        self.amount = amount
        self.description = description
        self.date = date if date else datetime.now().strftime("%Y-%m-%d")
        
    def to_dict(self):
        return {
            "id": self.id,
            "type": self.type,
            "category": self.category,
            "amount": self.amount,
            "description": self.description,
            "date": self.date
        }
    

def choose_category(transaction_type):
    if transaction_type == Transaction.INCOME:
        categories = [Transaction.SALARY, Transaction.INVESTMENTS, Transaction.GIFTS, Transaction.OTHER_INCOME]
    else:
        categories = [Transaction.FOOD, Transaction.TRANSPORT, Transaction.HOUSE, Transaction.ENTERTAINMENT, Transaction.OTHER_EXPENSE]

    print(f"\nВыберите категорию для {transaction_type}:\n")
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}\n")

    while True:
        try:
            choice = int(input("Введите номер категории: "))
            if 1 <= choice <= len(categories):
                return categories[choice - 1]
        except ValueError:
            print("Пожалуйста, введите корректный номер категории.")

def add_transaction(transactions):  # ← исправил на transactions
    print(f"\nДобавление Транзакции\n")
    print("1. Доход")
    print("2. Расход\n")

    while True:
        try:
            choice = int(input("Выберите тип транзакции (1 или 2): "))
            if choice == 1:
                transaction_type = Transaction.INCOME
                category = choose_category(transaction_type)
                amount = float(input("Введите сумму дохода: "))
                description = input("Введите описание (опционально): ")
                new_id = len(transactions) + 1
                transactions.append(Transaction(new_id, transaction_type, category, amount, description))
                print("Доход успешно добавлен!")
                break

            elif choice == 2:
                transaction_type = Transaction.EXPENSE
                category = choose_category(transaction_type)
                amount = float(input("Введите сумму расхода: "))
                description = input("Введите описание (опционально): ")
                new_id = len(transactions) + 1
                transactions.append(Transaction(new_id, transaction_type, category, amount, description))
                print("Расход успешно добавлен!")
                break

            else:
                print("Неверный выбор. Пожалуйста, введите 1 или 2.")

        except ValueError:
            print("Пожалуйста, введите корректное число.")

def show_balance(transactions):
    total_income = sum(t.amount for t in transactions if t.type == Transaction.INCOME)
    total_expense = sum(t.amount for t in transactions if t.type == Transaction.EXPENSE)
    balance = total_income - total_expense

    print(f"\nТекущий баланс: {balance:.2f} руб.\n")

def show_transactions(transactions):
    print("\nСписок всех транзакций:\n")
    
    for transaction in transactions:
        print(f"ID: {transaction.id}")
        print(f"Тип: {transaction.type}")
        print(f"Категория: {transaction.category}")
        print(f"Сумма: {transaction.amount:.2f} руб.")
        print(f"Дата: {transaction.date}")
        print(f"Описание: {transaction.description}")
        print("-" * 30)

def show_statistics(transactions):
    print("\nСТАТИСТИКА\n")
    # доходы по категориям
    income_by_category = {}
    for t in transactions:
        if t.type == Transaction.INCOME:
            income_by_category[t.category] = income_by_category.get(t.category, 0) + t.amount

    print("\nДоходы по категориям: \n")
    for category in income_by_category:
        print(f"\n{category}: {income_by_category[category]:.2f} руб.\n")


    # Суммируем расходы по категориям
    expenses_by_category = {}

    for transaction in transactions:
        if transaction.type == Transaction.EXPENSE:
            if transaction.category in expenses_by_category:
                expenses_by_category[transaction.category] += transaction.amount

            else:
                expenses_by_category[transaction.category] = transaction.amount

    print("\nСтатистика расходов по категориям:\n")

    for category, total in expenses_by_category.items():
        print(f"\n{category}: {total:.2f} руб.\n")

def save_transactions_to_file(transactions, filename="transactions.json"):

    transactions_data = [transaction.to_dict() for transaction in transactions]

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(transactions_data, file, ensure_ascii=False, indent=4)

    print(f"\nТранзакции успешно сохранены в файл {filename}.\n")

def load_transactions_from_file(filename="transactions.json"):

    if not os.path.exists(filename):
        print(f"Файл {filename} не найден. Создан новый список транзакций.")
        return []
    
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)
        return [Transaction(t["id"], t["type"], t["category"], t["amount"], t["description"], t["date"])
                for t in data]
    
    
def main():
    transactions = load_transactions_from_file()

    while True:
        print("\nМеню:\n")
        print("1. Добавить транзакцию")
        print("2. Показать баланс")
        print("3. Показать все транзакции")
        print("4. Показать статистику по категориям")
        print("5. Выйти\n")

        choice = input("Выберите действие: ")

        if choice == "1":
            add_transaction(transactions)
            save_transactions_to_file(transactions)
        elif choice == "2":
            show_balance(transactions)
        elif choice == "3":
            show_transactions(transactions)
        elif choice == "4":
            show_statistics(transactions)
        elif choice == "5":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите действие от 1 до 5.")

if __name__ == "__main__":
    main()