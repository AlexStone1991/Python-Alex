# TODO ООП. Ч8. Dataclasses. Урок 29.

from dataclasses import dataclass
from pprint import pprint

# class Book:
#     def __init__(self, name: str, weight: int, price: int):
#         self.name = name
#         self.weight = weight
#         self.price = price
#     def __repr__(self):
#         return f"Book(name={self.name}, weight={self.weight}, price={self.price})"

# b = Book("Учебник по Python 1", 100, 1800)
# print(b.name)

# @dataclass
# class BookData:
#     name: str
#     weight: int
#     price: int
# b1 = BookData("Учебник по Python 2", 100, 1800)
# print(b1.name)

# pprint(BookData.__dict__)

# ====================================================

# @dataclass
# class Person:
#     first_name: str = "Борис"
#     last_name: str = "Иванов"
#     age: int = 30
#     job: str = "Программист"

# p = Person()
# print(p)

# @dataclass
# class Developer:
#     first_name: str
#     last_name: str
#     age: int
#     job: str = "Developer"

# boris = Developer("Boris", "Ivanov", 30)
# ivan = Developer("Ivan", "Krasnov", 30)
# boray = Developer("Boris", "Ivanov", 30)
# print(ivan == boris)
# print(ivan)
# print(boris)
# print(boray == boris)
# misha = Developer("Michael", "Alexeev", 40, "Senior Developer")
# print(misha)
# senior_boray = ("Boris", "Ivanov", 30, "Senior Developer")
# print(senior_boray == boray)

# @dataclass
# class Doctor:
#     first_name: str
#     last_name: str
#     age: int
#     position: str
#     department: str
#     def __repr__(self):
#         return f"Doctor: {self.first_name} {self.last_name} ({self.age} лет, {self.position}, {self.department})"

# ivanov = Doctor("Alexander", "Ivanov", 37, "Surgeon", "Surgeon Department")

# print(ivanov)

# @dataclass
# class Student:
#     fname: str
#     lname: str
#     age: int
#     group: str
#     department: str = "IT"
#     def __eq__(self, other):
#         return self.lname == other.lname
#     def __repr__(self):
#         return f"Student: {self.fname} {self.lname}\n{self.age} лет\n{self.group}\n{self.department}"
# ivan = Student("Ivan", "Ivanov", 20, "Python")
# ivan3 = Student("Ivan", "Ivanov", 21, "Python2")
# print(ivan)
# print()
# print(ivan3)
# print(ivan == ivan3)

# @dataclass
# class BasicClass:
# __init__, __eq__, __repr__

from dataclasses import astuple, asdict


# ivan1 = Student("Ivan", "Ivanov", 20, "Python")
# print(astuple(ivan1))
# print(asdict(ivan1))

# dict1 = asdict(ivan1)
# tuplel = astuple(ivan1)
# print(dict1["age"])
# print(tuplel[3])

# @dataclass(frozen=True)
# class StudentF:
#     id: int = 234
#     fname: str = "Владимир"
#     lname: str = "Иванов"
#     age: int = 19
#     group: str = "A201"
#     department: str = "Кафедра Внешнего Естествознания"

# s1 = StudentF()
# s2 = StudentF(235, "Андрей", "Петров", 20, "A202", "Кафедра Внешнего Естествознания")
# print(s1)
# print(s2)

# class Book:
#     def __init__(self, name: str, weight: int, price: int, ls=[]):
#         self.name = name
#         self.weight = weight
#         self.price = price
#         self.ls = ls
#     def __repr__(self):
#         return f"Book = {self.__dict__}"

# b1 = Book("Учебник по Python", 100, 1800)
# b1.ls.append(10)
# print(b1)
# b2 = Book("Учебник по Python", 100, 1800)
# print(b2.ls)
# print(b2)
# b2.ls.append(30)
# print(b1.ls)
# print(b2.ls)
# print(b1)
# print(b2)

from  dataclasses import field

# @dataclass
# class BookDate:
#     name: str
#     weight: int
#     price: int
#     ls: list = field(default_factory=list)
# bd = BookDate("Учебник по Python", 100, 1800)
# bd.ls.append(10)
# bd1 = BookDate("Учебник по Python", 100, 1800)
# print(bd.ls)
# print(bd)
# print(bd1.ls)
# print(bd1)
# field(default=, default_factory=, init=, repr=, hash=, compare=, metadata=)

# @dataclass
# class Student:
#     id: int = 234
#     fname: str = "Владимир"
#     lname: str = "Иванов"
#     age: int = 19
#     group: str = "A201"
#     department: str = "Кафедра Внешнего Естествознания"
#     # full_name: str = field(init=False, repr=False)
#     # full_name: str = field(init=True, repr=True)
#     full_name: str = field(default="Y")
# s1 = Student()
# print(s1)
# s1.full_name = "X"
# print(s1)

# @dataclass
# class Student:
#     id: int = 234
#     fname: str = "Владимир"
#     lname: str = "Иванов"
#     age: int = 19
#     group: str = "A201"
#     department: str = "Кафедра Внешнего Естествознания"
#     full_name: str = field(init=False, repr=True)
#     def __post_init__(self):
#         self.full_name = self.fname + " " + self.lname
#         # self.full_name = f"{self.fname} {self.lname}"
# sd = Student()
# print(sd)
# print(sd.full_name)

# @dataclass(order=True)
# class Student1:
#     fname: str = "Владимир"
#     lname: str = "Иванов"
#     age: int = 19
#     group: str = "A201"
#     department: str = "Кафедра Внешнего Естествознания"
#     sort_age: int = field(init=False, repr=False)
#     def __post_init__(self):
#         self.sort_age = self.age
#         # self.full_name = f"{self.fname} {self.lname}"
# s1 = Student1(age = 20)
# s2 = Student1(age = 21)
# print(s1 > s2)
# print(s1 < s2)

# class Vector:
#     def __init__(self, x: int, y: int, z: int):
#         self.x = x
#         self.y = y
#         self.z = z
#         self.l = (x**2 + y**2 + z**2)**0.5
# @dataclass
# class Vr:
#     x: int
#     y: int
#     z: int
#     l: float = field(init=False)
#     def __post_init__(self):
#         self.l = (self.x**2 + self.y**2 + self.z**2)**0.5

# v1 = Vector(1, 2, 3)
# v2 = Vr(1, 2, 3)

# print(v1)
# print(v1.l)
# print(v2)

@dataclass
class Vr:
    x: int = field(repr=False)
    y: int
    z: int = field(compare=False)
    l: float = field(init=False, compare=False)
    def __post_init__(self):
        self.l = (self.x**2 + self.y**2 + self.z**2)**0.5

v1 = Vr(1, 2, 3)
v2 = Vr(1, 2, 3)
print(v1 == v2)
v3 = Vr(1, 2, 4)
v4 = Vr(1, 2, 9)
print(v3 == v4)




