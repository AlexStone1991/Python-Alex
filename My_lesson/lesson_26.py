# TODO ООП Ч5. Наследование. Abstractmethod. Super. Переопределение и расширение. Урок 26

# концепция наследования
# Как называются родиьельсие классы и наследники
# - Базовый класс и производный класс
# - Родительсукий класс
# - super 
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
    pass

dog = Dog("Шарик")
cat = Cat("Барсик")

print(dog.voice())  # Вызовет метод voice из Dog
print(cat.voice())