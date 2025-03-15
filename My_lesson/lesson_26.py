# TODO ООП Ч5. Наследование. Abstractmethod. Super. Переопределение и расширение. Урок 26

# концепция наследования
# Как называются родиьельсие классы и наследники
# - Базовый класс и производный класс
# - Родительсукий класс
# - Superclass и subclass
# преопрелделение методов
# расширение методов
# Вызов методов родительского класса
# Super
# работа с инцилизаторами

# 1. Концепция наследования
# Наследование это механизм, который позволяет создать новы класс на основе уже существующего.

class Animal:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f'{self.__class__.__name__} по имени {self.name}'
    def voice(self):
        return f"{self.__class__.__name__} по имени {self.name} издал(а) звук"

class Dog(Animal):
    # пайтон ищет методо у собственного класса
    # тут мы переопределяем методо voice( у класса Dog)
    # теперь будети вызываться метод voice у класса dog а не у класса animal
    def voice(self):
        # result = Animal.voice(self)
        result = super().voice()  # вызовет родительский метод voice у Animal
        return f"{result}, это было сделано собакой"


class Cat(Animal):
    def __init__(self, name: str, fluffy_level: int):
        super().__init__(name)
        self.fluffy_level = self.__fluffy_validator(fluffy_level)

    def voice(self):
        return f"{super().voice()} и это было сделано кошкой, и уровень пушистости {self.fluffy_level}"

    def __fluffy_validator(self, fluffy_level):
        if not 0 <= fluffy_level <= 10:
            raise ValueError("Fluffy level should be between 0 and 10")
        else:
            return fluffy_level

dog = Dog("Шарик")
cat = Cat("Мурка", 5)

print(dog.voice())  # Вызовет метод voice из Dog
print(cat.voice())

# MRO - Method Resolution Order - порядок разрешения методов
# Порядок разрешения методов это порядок в котором Python ищет в иерархии наследованимя

# Получим этот для Dog
print(Dog.__mro__)

# (<class "__main__.Dog">, <class "__main__.Animal">, <class "object">)