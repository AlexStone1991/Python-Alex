# TODO ООП 11. Паттерны проектирования. Ч2. Урок 33.

from abc import ABC, abstractmethod
from dataclasses import dataclass, field

"""
Абстрактная фабрика на примере имтации библиотеки работы с разными БД
SQLite
PostgreSQL

Продукты
Простой запрос в БД
Вызов оконной функции

описание классов
Абстрактная фабрика SQL подключения 
фабрика для SQLite
фабрика для PostgreSQL

Абстрактный класс для простого запроса
абстрактный класс для оконной функции
простой запрос для SQLite
простой запрос для PostgreSQL
оконная функция для SQLite
оконная функция для PostgreSQL
"""

# Абстрактный продукт простой SQL-запрос
class AbstractSimpleQuery(ABC):
    @abstractmethod
    def execute(self):
        pass

# Абстрактный продукт оконной функции SQL
class AbstractWindowFunction(ABC):
    @abstractmethod
    def execute_window_function(self):
        pass

# Реальный продукты простой SQL-запрос для SQLite
class SQLiteSimpleQuery(AbstractSimpleQuery):
    def execute(self):
        print(f"Выполняем простой SQL запрос для SQLite классом : {self.__class__.__name__}")

# Реальный продукты простой SQL-запрос для PostgreSQL
class PostgreSQLSimpleQuery(AbstractSimpleQuery):
    def execute(self):
        print(f"Выполняем простой SQL запрос для PostgreSQL классом : {self.__class__.__name__}")

# Реальный продукты оконной функции для SQLite
class SQLiteWindowFunction(AbstractWindowFunction):
    def execute_window_function(self):
        print(f"Выполняем оконную функцию для SQLite классом : {self.__class__.__name__}")

# Реальный продукты оконной функции для PostgreSQL
class PostgreSQLWindowFunction(AbstractWindowFunction):
    def execute_window_function(self):
        print(f"Выполняем оконную функцию для PostgreSQL классом : {self.__class__.__name__}")

# Абстрактная фабрика SQL подключения
class AbstractSQLConnectionFactory(ABC):
    @abstractmethod
    def create_simple_query(self) -> AbstractSimpleQuery:
        pass

    @abstractmethod
    def create_window_function(self) -> AbstractWindowFunction:
        pass

# фабрика подключения к SQLite
class SQLiteConnectionFactory(AbstractSQLConnectionFactory):
    def create_simple_query(self) -> AbstractSimpleQuery:
        return SQLiteSimpleQuery()
    def create_window_function(self) -> AbstractWindowFunction:
        return SQLiteWindowFunction()

# фабрика подключения к PostgreSQL
class PostgreSQLConnectionFactory(AbstractSQLConnectionFactory):
    def create_simple_query(self) -> AbstractSimpleQuery:
        return PostgreSQLSimpleQuery()
    def create_window_function(self) -> AbstractWindowFunction:
        return PostgreSQLWindowFunction()
    
# пример использования
def main():
    # Словарь фабрик подключений
    factories = {
        "sqlite": SQLiteConnectionFactory,
        "postgresql": PostgreSQLConnectionFactory
    }
    # выболр фабрики подключения
    choise = input("Выберите тип БД (sqlite/postgresql): ").strip().lower()
    factory = factories.get(choise)
    if not factory:
        print("Неправильный выбор БД")
        return
    # создание фабрики подключения
    connection_factory = factory()
    simple_query = connection_factory.create_simple_query()
    window_function = connection_factory.create_window_function()
    # выполнение простого SQL
    simple_query.execute()
    # выполнение оконной функции SQL
    window_function.execute_window_function()

if __name__ == "__main__":
    main()