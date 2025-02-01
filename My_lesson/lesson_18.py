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

a = 2
# nonlocal
def foo():
    a = 3 #Local foo
    print(f"foo до вызова foo2: {a=}")

    def foo2():
        nonlocal a  # позволит переписать а из foo если выключено будет а = 3, если включено будет а = 4
        a = 4
        print(f'foo2: {a=}')

    foo2()
    print(f"foo после вызова foo2: {a=}")

foo()

