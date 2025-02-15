# TODO ООП. Ч1. Атрибуты и методы. Класс и экземпляр. Практика. Урок 22.

#  - class
# - нейминг классов UpperCamelCase
# - __init__ - иницилизатор
#  - self - ссылка на экземпляр класса

class Person:
    def __init__(self, name: str):
        self.name = name
    def say_my_name(self):
        print(f"Привет, меня зовут {self.name}!")

p1 = Person("Барак")
p2 = Person("Владимир") 
p3 = Person("Джордж")

print(p1.name, p2.name, p3.name)
p1.say_my_name()
p2.say_my_name()
p3.say_my_name()



