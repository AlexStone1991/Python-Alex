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
# Модуль ABC - Abstract base classes
# Декаратор @abstractmethod

from abc import ABC, abstractmethod

# class AbstractDocument(ABC):
#     def __init__(self, file_path: str, encoding:str="utf-8"):
#         self.file_path = file_path
#         self.encoding = encoding

#     @abstractmethod
#     def read(self):
#         pass
    
#     @abstractmethod
#     def write(self):
#         pass

#     @abstractmethod
#     def append(self):
#         pass

#     def __str__(self):
#         return f"Документ типа {self.__class__.__name__} по пути {self.file_path}"
    
# class TextDocument(AbstractDocument):
#     def read(self)-> list[str]:
#         with open(self.file_path, "r", encoding=self.encoding) as file:
#             clear_data = [string.strip() for string in file.readlines()]
#             return clear_data
#     def write(self) -> None:
#         with open(self.file_path, "w", encoding=self.encoding) as file:
#             write_data = "\n".join(data)
#             file.write(write_data)
#     def append(self, *data: str) -> None:
#         with open(self.file_path, "a", encoding=self.encoding) as file:
#             write_data = "\n".join(data)
#             file.write(write_data)

# document = TextDocument("test.txt")
# document.write("Привет", "Мир")
# print(document.read())

# Иерархическое наследование - когда один класс наследует от нескольких классов
# Множественное наследование - когда один класс наследует от нескольких класс

class A:
    def method_a(self):
        print('Метод A')

class B:
    def method_b(self):
        print('Метод B')

class C(A, B):
    def method_c(self):
        print('Метод C')

print(C.__mro__)

# Бабка - Жучка - Внучка - Репка

# Репка - базовый класс

# class Repka:
#     def __init__(self, weight):
#         self.weight = weight

#     def __str__(self):
#         return f'Репка весом {self.weight} кг'

#     def pull(self):
#         print('Тянут репку')


# # Бабка - класс наследник от Репка
# class Babka(Repka):
#     def __init__(self, weight, name):
#         super().__init__(weight)
#         self.name = name

#     def __str__(self):
#         return f'Бабка {self.name} весом {self.weight} кг'

#     def pull(self):
#         print('Бабка тянет репку')

# # Жучка - класс наследник от Репка
# class Zhuchka(Repka):
#     def __init__(self, weight, name):
#         super().__init__(weight)
#         self.name = name

#     def __str__(self):
#         return f'Жучка {self.name} весом {self.weight} кг'

#     def pull(self):
#         print('Жучка тянет репку')