# TODO Функции Ч6. Декаораторы. Параметры декоратора. Урок 19
from typing import Callable, Any, List, Dict, Tuple, Set, Iterable, Union, Optional
"""
def simple_decorator(func: Callable):
    def wrapper():
        print(f"печать до вызова.")
        result = func()
        print(f"печать после вызова.")
        return result
    return wrapper

@simple_decorator
def foo():
    return f'Результат foo'

@simple_decorator
def foo66():
    return f'Функция 66'

print(foo())
print(foo())
print(foo())
"""

"""
str - строка
int - целое число
float - число с плавающей точкой
bool - True или False
list - list() - список
tuple - tuple() - кортеж
set - set() - множество
None - нет значения
dict - словарь


list[str] - списко строк
set[str] - множество из строк
| - ИЛИ

Расширенные аннтотации типов Typing

Any - любой тип данных
Callable - callable объект
Iterable - итерируемый объект
Union - объединение тиов - ИЛИ то или ЭТО
Optional - или ЭТО или None
Dict[[str|int], List[Union[str, None]]] - словарь, где ключи - строки, значения - список строк или целых чисел
Callable[[int, str], str] - функция, принимающая целое число и строку, и возвращающая строку
Iterable[str] - итерируемый объект, содержащий строки
Optional[int] - целое число или None
Union[int, float] - целое или число с плавающей точкой
"""
# def multiply(a: int, b: int):
#     return a * b

# def get_sum(num_list: List[int]) -> int:
#     return sum(num_list)

# print(multiply(5, 6))
# print(multiply(5, "6"))

# data_set = ["1", "2", "3", "4","5", "6"]
# print(get_sum(data_set)) #функция с ошибкой для проверки mypy расширения

# ===============Декораторы===================
def simple_decorator2(func: Callable):
    def wrapper(*args, **kwargs):
        print(f"печать до вызова.")
        result = func(*args, **kwargs)
        print(f"печать после вызова.")
        return result
    return wrapper

@simple_decorator2
def multiply2(a: int, b: int) -> int:
    return a * b
@simple_decorator2
def multiple3(a: int, b: int, c: int) ->int:
    return a * b * c

print(multiply2(5, 6))
print(multiple3(5, 6, 7))

"""
ВАРИАНТЫ АННОТАЦИЙ ДЛЯ ДЕКОРАТОРОВ С ARGS/KWARGS:

1. Базовый вариант (любые аргументы, любой возврат):
def decorator(func: Callable[..., Any]) -> Callable[..., Any]

2. Строгая типизация конкретных аргументов:
def decorator(func: Callable[[int, str], bool]) -> Callable[[int, str], bool]

3. Смешанный вариант (известны типы позиционных аргументов):
def decorator(func: Callable[[int, str, ...], str]) -> Callable[[int, str, ...], str]

4. С указанием типов для kwargs:
def decorator(func: Callable[..., Dict[str, Any]]) -> Callable[..., Dict[str, Any]]

5. Комбинированный вариант:
def decorator(func: Callable[[int, str], Union[str, None]]) -> Callable[[int, str], Union[str, None]]

6. Для методов класса:
def decorator(func: Callable[[Any, ...], Any]) -> Callable[[Any, ...], Any]

7. Для асинхронных функций:
def decorator(func: Callable[..., Awaitable[Any]]) -> Callable[..., Awaitable[Any]]

8. С параметрами декоратора:
def param_decorator(param: str) -> Callable[[Callable[..., Any]], Callable[..., Any]]

ВАЖНО: ... в Callable означает "любое количество аргументов любого типа"
"""
from time import perf_counter
from marvel import full_dict

def timer_decorator(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        result = func(*args, **kwargs)
        end_time = perf_counter()
        print(f"Время выполнения функции {func.__name__}: {end_time - start_time:.10f} сек.")
        return result
    return wrapper
@timer_decorator
def get_film_by_year(year: int) -> List[Dict[str, Any]]:
    return [film for film in full_dict.values() if film["year"] == year]
print(get_film_by_year(2008))

@timer_decorator
def foo():
    return f"Результат foo"
@timer_decorator
def foo66():
    return f"Функция 66"

print(foo())
print(foo())
print(foo())

print(foo66())
print(foo66())
print(foo66())

################# Декоратор с парамером################
"""
декоратор проверяющий длину строки и выдающий ошибку если длина строки не соотвествует параметру
"""
def string_length_decorator(min_length: int) -> Callable:
    def decorator(func: Callable[[str], str]) -> Callable[[str], str]:
        def wrapper(name: str) -> str:
            if len(name) < min_length:
                raise ValueError(f"Строка {name} слишком короткая. Длина должна быть не менее {min_length} символам.")
            return func(name)
        return wrapper
    return decorator

@string_length_decorator(5)
def hello(name: str) -> str:
    return f"Привет, {name}!"

# print(hello("Alex"))
print(hello("Евгений"))

while True:
    name = input("Введите ваше имя: ")
    try:
        print(hello(name))
        break
    except ValueError as error:
        print(error)