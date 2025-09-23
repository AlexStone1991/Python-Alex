# TODO Функции. Ч5. Области видимости. Замыкания. Декаратор. Урок 18
# TODO  Запушить репозиторий свой на гид - git push -u origin main.
# области видимости в python
# Built-in - встроенная - служебная область видимости Python
# - print() -len() -bool()

# Global -глобальная область видимости
# Все переменные созданные вне функции принадлежат глобальной области видимости

# Local - локальная область видимости
# Nonlocal - не локальная область видиомсти (функции внутри функции)

# python производит поиск "изнутри наружу".

# # Это Глабальная работа Global
# print = "банан"
# print("Апельсин") - это был эксперимент

# print(banana) - NameError: name 'banana' is not defined

# a = 2 # Global
# def foo():
#     # Это локальная работа Local
#     a = 10
#     print(f"foo: {a=}")

# def foo2():
#     global a  # Эта локальная работа Local, но меняет глобальную переменную
#     a = 4 #local
#     print(f"foo2: {a=}")

# def foo3():
#     print(f"foo3: {a=}")

# print(a) # Global
# foo() #Local
# foo2() #Local
# foo3() #Global после как добавили в def foo2 global a изменился результат! стало 4
# print(a) #Global

# a = 2
# # nonlocal
# def foo():
#     a = 3 #Local foo
#     print(f"foo до вызова foo2: {a=}")

#     def foo2():
#         nonlocal a  # позволит переписать а из foo если выключено будет а = 3, если включено будет а = 4
#         a = 4
#         print(f'foo2: {a=}')

#     foo2()
#     print(f"foo после вызова foo2: {a=}")

# foo()

# bananas = print

# bananas("Привет") # Это вызов встроенной функции print()
# bananas("как дела?")

# one = "1"
# bir = one
# odin = bir

# print(odin)

# nonlocal
def foo(a: str):
    # a - local для foo
    def foo2():
        return a
    return foo2

f2 = foo("Апельсин")
f3 = foo("банан")

orange = f2() # Замыкание.
banan = f3()

print(orange)
print(banan)

# f2 -> foo2 -> "апельсин" (local a)
# banan -> foo2 -> a(банан)
# banan() - мы получаем строку, которая хранилась в локальной области внешней функции

# Счетчик функция
def counter(start: int = 0, step: int = 1):

    position = start

    def tik():
        nonlocal position
        position += step
        return position
    
    return tik

counter_0_2 = counter(0, 2)
print(counter_0_2())# 2
print(counter_0_2())# 4
print(counter_0_2())# 6
print(counter_0_2())
print(counter_0_2())
print(counter_0_2())
print(counter_0_2())
print(counter_0_2())
print(counter_0_2())# 18


product_list = ["морковь", "картошка", "чеснок", "говядина", "коньяк"]

"""
СОРТИРОВЩИК ПО АЛФАВИТУ Версия 1
def product_sort(products: list):
    # тут будет хранится products
    cach = []

    def sorter():
        nonlocal cach
        if cach and len(cach) == len(products):
            return cach
        
        cach = sorted(products)
        return cach

    return sorter

product_sorter = product_sort(product_list)
print(product_sorter())
print(product_sorter())

product_list.append("капуста")
print(product_sorter())
print(product_sorter())
"""
from typing import Callable
# Сортировщик Версия 2
def get_sorter():
    cach = []

    def sorter(data_list: list):
        nonlocal cach
        if cach and len(cach) == len(data_list):
            return cach
        
        cach = sorted(data_list)
        return cach
    
    return sorter

product_sorter = get_sorter()
print(product_sorter(product_list))
print(product_sorter(product_list))

product_list.append("капуста")
print(product_sorter(product_list))
print(product_sorter(product_list))

def use_built_in_func(func: Callable, data_list: list):
    print(func(data_list))

use_built_in_func(len, product_list)
use_built_in_func(sorted, product_list)
use_built_in_func(sum, [1,2,3,4])

def simple_decorator(func: Callable, message: str):
    def wrapper():
        print(f"печать до вызова. {message}")
        func()
        print(f"печать после вызова. {message}")
    return wrapper

def foo():
    print("вызов foo")

foo_decorated = simple_decorator(foo, "Привет")
foo_decorated()
        