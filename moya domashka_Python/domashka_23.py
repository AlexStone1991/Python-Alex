from typing import Callable

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