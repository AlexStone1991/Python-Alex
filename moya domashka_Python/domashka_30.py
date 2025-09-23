from abc import ABC, abstractmethod

# Абстрактный интерфейс для всех стратегий проверки палиндромов
class PalindromeStrategy(ABC):
    @abstractmethod
    def is_palindrome(self, text: str) -> bool:
        pass

# Конкретная реализация стратегии для проверки одиночных слов
class SingleWordPalindrome(PalindromeStrategy):
    def is_palindrome(self, text: str) -> bool:
        # Проверка, является ли отдельное слово палиндромом
        cleaned_text = text.lower()
        return cleaned_text == cleaned_text[::-1]
    
# Конкретная реализация стратегии для проверки многословных выражений
class MultiWordPalindrome(PalindromeStrategy):
    def is_palindrome(self, text: str) -> bool:
        # Проверка, является ли выражение палиндромом, игнорируя пробелы и регистр
        cleaned_text = ''.join(text.split()).lower()
        return cleaned_text == cleaned_text[::-1]

# Класс, отвечающий за использование текущей стратегии
class PalindromeContext:
    def __init__(self, strategy: PalindromeStrategy):
        self.strategy = strategy
    
    def set_strategy(self, strategy: PalindromeStrategy) -> None:
        self.strategy = strategy

    def check(self, text: str) -> bool:
        return self.strategy.is_palindrome(text)
    
# Фасад для упрощения работы с проверкой палиндромов
class PalindromeFacade:
    def __init__(self):
        self.context = PalindromeContext(SingleWordPalindrome())

    def check_palindrome(self, text: str) -> bool:
        # Определяет, какое правило проверки применить (слово или выражение) и проводит проверку через PalindromeContext
        if len(text.split()) == 1:
            self.context.set_strategy(SingleWordPalindrome())
        else:
            self.context.set_strategy(MultiWordPalindrome())
        return self.context.check(text)
    
# Тестирование
if __name__ == "__main__":
    facade = PalindromeFacade()
    
    # Тест 1: Одиночное слово-палиндром
    word = "Racecar"
    print(f"'{word}' — палиндром? {facade.check_palindrome(word)}")  # True

    # Тест 2: Одиночное слово не палиндром
    word = "Python"
    print(f"'{word}' — палиндром? {facade.check_palindrome(word)}")  # False

    # Тест 3: Многословное выражение-палиндром
    phrase = "A man a plan a canal Panama"
    print(f"'{phrase}' — палиндром? {facade.check_palindrome(phrase)}")  # True

    # Тест 4: Многословное выражение не палиндром
    phrase = "Hello World"
    print(f"'{phrase}' — палиндром? {facade.check_palindrome(phrase)}")  # False

    # Тест 5: Одно слово с разными регистрами
    word = "Deified"
    print(f"'{word}' — палиндром? {facade.check_palindrome(word)}")  # True

    # Тест 6: Сложная фраза с пробелами
    phrase = "Was it a car or a cat I saw"
    print(f"'{phrase}' — палиндром? {facade.check_palindrome(phrase)}") #True
    
    # Тест 7: Сложная фраза с разными регистрами
    phrase = "Madam, in Eden, I'm Adam"
    print(f"'{phrase}' — палиндром? {facade.check_palindrome(phrase)}") #False

    # Тест 8: Сложная фраза с разными регистрами и пробелами
    phrase = "WaS iT a Car oR a cAt I sAw"
    print(f"'{phrase}' — палиндром? {facade.check_palindrome(phrase)}") #True
    
    # Тест 9: Строка с числами
    numbers = "12321"
    print(f"'{numbers}' — палиндром? {facade.check_palindrome(numbers)}")  # True

    # Тест 10: Строка с числами и буквами
    mixed = "A1b2b1A"
    print(f"'{mixed}' — палиндром? {facade.check_palindrome(mixed)}")  # True

    # Тест 12: Строка с разными регистрами и пробелами и знаками
    mixed_case_spaces = "No 'x' in Nixon"
    print(f"'{mixed_case_spaces}' — палиндром? {facade.check_palindrome(mixed_case_spaces)}") #False

"""
'Racecar' — палиндром? True
'Python' — палиндром? False
'A man a plan a canal Panama' — палиндром? True
'Hello World' — палиндром? False
'Deified' — палиндром? True
'Was it a car or a cat I saw' — палиндром? True
'Madam, in Eden, I'm Adam' — палиндром? False
'WaS iT a Car oR a cAt I sAw' — палиндром? True
'12321' — палиндром? True
'A1b2b1A' — палиндром? True
'No 'x' in Nixon' — палиндром? False
"""

#P.S. Не сколько строк добавил от себя)))
