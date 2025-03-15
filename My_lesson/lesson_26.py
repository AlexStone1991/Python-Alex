# TODO ООП Ч5. Наследование. Abstractmethod. Super. Переопределение и расширение. Урок 26

# концепция наследования
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
        print(f"{self.__class__.__name__} по имени {self.name} издал(а) звук")

class Dog(Animal):
    def voice(self):
        print(f"{self.__class__.__name__} по имени {self.name} начал(а) лаять")

class Cat(Animal):
    def voice(self):
        return super()

dog = Dog("Шарик")
cat = Cat("Барсик")

dog.voice()  # Вызовет метод voice из Dog
cat.voice()