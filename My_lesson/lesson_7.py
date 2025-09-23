# TODO Урок 7. Методы списков. Циклы

# Методы и функции для работы с списками

# len(list) - возвращает длину списка
# max(list) - возвращает максимальный элемент списка
# min(list) - возвращает минимальный элемент списка
# sum(list) - возвращает сумму элементов списка
# sorted(list) - возвращает новый отсортированный список
# bool(list) - возвращает True, если список не пустой, и False, если список пустой
 
 
# list.append(item) - добавляет элемент в конец списка
# list.extend(iterable) - добавляет элементы из итерируемого объекта в конец списка
# list.insert(index, item) - вставляет элемент по указанному индексу
# list.remove(item) - удаляет первый элемент со значением item из списка
# list.pop(index) - удаляет элемент по указанному индексу и возвращает его
# list.clear() - удаляет все элементы из списка
# list.index(item) - возвращает индекс первого элемента со значением item
# list.count(item) - возвращает количество элементов со значением item в списке
# list.sort() - сортирует список по возрастанию
# list.reverse() - разворачивает список

names_list = ["Антон", "Анна", "Андрей", "Алексей", "Анастасия"]

names_list.sort()
print(names_list)

print(max(names_list))
print(min(names_list))

# Сортировка списка по длине имени
names_list.sort(key=len, reverse=True)
print(names_list)

# список чисел
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum(numbers_list))
print(max(numbers_list))
print(min(numbers_list))

# нам надо понять есть ли имена длинее 10 символов
is_long_name = False

for name in names_list:
    if len(name) >= 10:
        is_long_name = True
        print("Есть имя длинее 10 символов")
        break
else:
    print("Нет имя длинее 10 символов")

long_name = [name for name in names_list if len(name) >= 10]
if long_name:
    print("Есть имя длинее 10 символов")
else:
    print("Нет имя длинее 10 символов")

# добавление в список
# append - добавляет элемент в конец списка
# extend - добавляет элементы из итерируемого объекта в конец списка
# insert - вставляет элемент по указанному индексу

names_list = ["Антон", "Анна", "Андрей", "Алексей", "Анастасия"]
# добавляем в конец списка
names_list.append("Елена")

# Добавлнием в начало списка
names_list.insert(0, "Алексей")

# PRACTICE Практика топ3 имён
"""
1. Объявите пустой список names_list
2. Объявите цикл while true и в нём получите от пользователя имя
3. Если длина списка равна 3 или более - добавьте имя под индексом 0
4. Удалите последний элемент списка list.pop()
5. Если длина списка меньше 3 - добавьте имя в конец списка
6. Выведите список на экран
 
"""

# names_list = []

# while True:
#     name = input("Введите имя: ")
#     if name == "стоп" or name == "":
#         break
    
#     if len(names_list) >= 3:
#         names_list.insert(0, name)
#         names_list.pop()
#     else:
#         names_list.append(name)
#     print(names_list)

product_list = ["яблоко", "банан", "апельсин", "яблоко", "банан", "яблоко"]
# удаление элемента по назначению
product_list.remove("банан")
print(product_list)
print(product_list.pop(1))

product_list_2 = product_list.copy()
product_list[0] = "Киви"
print(product_list_2)


# Set - множество
# Множество - это неупорядоченная коллекция неизменяймых уникальных элементов
# Неизменяемые - строки, числа, кортежи, bool None

a = "1"
b = 2
c = 3

print(hash(a))
print(hash(b))
print(hash(c))

