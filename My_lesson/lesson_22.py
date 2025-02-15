# TODO ООП. Ч1. Атрибуты и методы. Класс и экземпляр. Практика. Урок 22.

#  -class
# - нейминг классов UpperCamelCase



class Person:
    pass

p1 = Person() # <__main__.Person object at 0x00000271D2DE6E40>
p2 = Person() # <__main__.Person object at 0x00000271D3064E10>

p1.name = "Филлип"
p2.name = "Джордж"

print(p1.name, p2.name)

