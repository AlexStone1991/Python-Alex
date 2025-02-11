from typing import Callable
import csv
# Шаг 1: Создаем декоратор password_checker
# Декоратор будет проверять пароль на соответствие следующим критериям:

# Минимальная длина: 8 символов.
# Содержит хотя бы одну цифру.
# Содержит хотя бы одну заглавную букву.
# Содержит хотя бы одну строчную букву.
# Содержит хотя бы один специальный символ.
def password_checker(func: Callable) -> Callable:
    """
    Декоратор для проверки сложности пароля.
    """
    def wrapper(password: str) -> str:
        # Проверка длины пароля
        if len(password) < 8:
            return "Ошибка: Пароль должен содержать минимум 8 символов."
        
        # Проверка наличия цифры
        if not any(char.isdigit() for char in password):
            return "Ошибка: Пароль должен содержать хотя бы одну цифру."
        
        # Проверка наличия заглавной буквы
        if not any(char.isupper() for char in password):
            return "Ошибка: Пароль должен содержать хотя бы одну заглавную букву."
        
        # Проверка наличия строчной буквы
        if not any(char.islower() for char in password):
            return "Ошибка: Пароль должен содержать хотя бы одну строчную букву."
        
        # Проверка наличия специального символа
        special_chars = "!@#$%^&*()_+=-[]{};:'\"\\|,.<>/?"
        if not any(char in special_chars for char in password):
            return "Ошибка: Пароль должен содержать хотя бы один специальный символ."
        
        # Если все проверки пройдены, вызываем оригинальную функцию
        return func(password)
    
    return wrapper

# Шаг 2: Создаем функцию register_user
# Функция будет регистрировать пользователя, если пароль прошел проверку.

@password_checker
def register_user(password: str) -> str:
    """
    Функция для регистрации пользователя.
    """
    return "Регистрация прошла успешно!"

# Шаг 3: Тестируем

# Тестирование успешного случая
print(register_user("Password123!"))  # Регистрация прошла успешно!

# Тестирование неудачных случаев
print(register_user("pass"))          # Ошибка: Пароль должен содержать минимум 8 символов.
print(register_user("password"))      # Ошибка: Пароль должен содержать хотя бы одну цифру.
print(register_user("PASSWORD123"))   # Ошибка: Пароль должен содержать хотя бы одну строчную букву.
print(register_user("password123"))   # Ошибка: Пароль должен содержать хотя бы одну заглавную букву.
print(register_user("Password123"))   # Ошибка: Пароль должен содержать хотя бы один специальный символ.

# Часть 2: Декораторы для валидации данных и сохранения в CSV
# Шаг 1: Создаем декоратор password_validator
# Этот декоратор будет более гибким, позволяя задавать параметры для проверки пароля.

def password_validator(
    min_length: int = 8,
    min_uppercase: int = 1,
    min_lowercase: int = 1,
    min_special_chars: int = 1
) -> Callable:
    """
    Декоратор для валидации пароля.
    """
    def decorator(func: Callable) -> Callable:
        def wrapper(username: str, password: str) -> str:
            # Проверка длины пароля
            if len(password) < min_length:
                raise ValueError(f"Пароль должен содержать минимум {min_length} символов.")
            
            # Проверка количества заглавных букв
            if sum(1 for char in password if char.isupper()) < min_uppercase:
                raise ValueError(f"Пароль должен содержать минимум {min_uppercase} заглавных букв.")
            
            # Проверка количества строчных букв
            if sum(1 for char in password if char.islower()) < min_lowercase:
                raise ValueError(f"Пароль должен содержать минимум {min_lowercase} строчных букв.")
            
            # Проверка количества специальных символов
            special_chars = "!@#$%^&*()_+=-[]{};:'\"\\|,.<>/?"
            if sum(1 for char in password if char in special_chars) < min_special_chars:
                raise ValueError(f"Пароль должен содержать минимум {min_special_chars} специальных символов.")
            
            # Если все проверки пройдены, вызываем оригинальную функцию
            return func(username, password)
        
        return wrapper
    
    return decorator

# Шаг 2: Создаем декоратор username_validator
# Этот декоратор будет проверять, что в имени пользователя нет пробелов.

def username_validator(func: Callable) -> Callable:
    """
    Декоратор для валидации имени пользователя.
    """
    def wrapper(username: str, password: str) -> str:
        if ' ' in username:
            raise ValueError("Имя пользователя не должно содержать пробелов.")
        return func(username, password)
    
    return wrapper

# Шаг 3: Создаем функцию register_user с сохранением в CSV

@username_validator
@password_validator(min_length=10, min_uppercase=2, min_lowercase=2, min_special_chars=2)
def register_user(username: str, password: str) -> str:
    """
    Функция для регистрации пользователя и сохранения данных в CSV файл.
    """
    with open("users.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([username, password])
    
    return "Регистрация прошла успешно!"

# Шаг 4: Тестируем

# Тестирование успешного случая
try:
    print(register_user("JohnDoe", "Password123!!"))
except ValueError as e:
    print(f"Ошибка: {e}")

# Тестирование неудачного случая по паролю
try:
    print(register_user("JaneDoe", "pass"))
except ValueError as e:
    print(f"Ошибка: {e}")

# Тестирование неудачного случая по юзернейму
try:
    print(register_user("Jane Doe", "Password123!!"))
except ValueError as e:
    print(f"Ошибка: {e}")