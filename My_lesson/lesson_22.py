# TODO ООП. Ч1. Атрибуты и методы. Класс и экземпляр. Практика. Урок 22.

#  -class
# - нейминг классов UpperCamelCase

class Person:
    # Атрибут класса
    name = "Alexander"

p1 = Person()
p2 = Person() 

print(p1.name, p2.name)

p1.name = "Филлип"
p2.name = "Джордж"

print(p1.name, p2.name)

