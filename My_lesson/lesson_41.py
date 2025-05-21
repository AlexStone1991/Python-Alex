# TODO SQL на Python Ч1. Sqlite3. Урок 41

import sqlite3 as s13
from tabulate import tabulate


SQL_SCRIPT = r"C:/ALEXXX/Python-Alex/My_lesson/lesson_39_2.sql"
DB_FILE = r"C:/ALEXXX/Python-Alex/Data/students_new.db"
"""
КОД ВЫПОЛНИТЬ ОДИН РАЗ!!!

# 1. Читамем SQL файл и берем скрипты на создание таблиц и наполнение данными
with open(SQL_SCRIPT, "r", encoding="utf=8") as sql_file:
    sql_script = sql_file.read()
"""
# 2. создание подлючение к базе данных
# connection = s13.connect(DB_FILE)
"""
# 3. создаем курсор для выполенения
cursor = connection.cursor()

# 4. Выполняем SQL скрипт
cursor.executescript(sql_script)

# 5. Закрываем курсор и соединение
cursor.close()
connection.close()
"""

def get_data_from_table(connection: s13.Connection, sql_query: str) -> tuple:
    
    # Создаем курсор набазе соедигнения полученного в аргументе функции
    cursor = connection.cursor()
    try:
        # Выполенение SQL запроса
        cursor.execute(sql_query)
        # Получаем все строки результата запроса
        data = cursor.fetchall()
        # Получаем названия столбцов из таблицы
        colomns = cursor.description
        colomns_list = [column[0] for column in colomns]
        return data, colomns_list
    
    except s13.Error as error:
        print(error)
        raise #Передаем исключение выше, что бы обрабывать его в вызывающем коде
    finally:
        # закрываем курсор
        cursor.close()

def render_table(data: list, columns: list, table_style: str = "grid") -> str:
    """
    Функция для форматирования данных в виде таблицы с использованием библиотеки tabulate
    :param data: список строк данных
    :param columns: список названий столбцов
    :param table_style: стиль таблицы
    :return: таблица в виде строки
    """
    return tabulate(data, headers=columns, tablefmt=table_style, stralign="center", numalign="center")
    

connection = s13.connect(DB_FILE)

SQL_SCRIPT1 = "SELECT * FROM students"
SQL_SCRIPT2 = "SELECT * FROM teachers"
SQL_SCRIPT3 = "SELECT * FROM groups"

sql_scripts = [SQL_SCRIPT1, SQL_SCRIPT2, SQL_SCRIPT3]

for sql_script in sql_scripts:
    print(render_table(*get_data_from_table(connection, sql_script)))


def create_student(connection: s13.Connection, **student_data: str|int) -> None:

    cursor = connection.cursor()

    main_fields = ["first_name", "last_name"]
    if not all(field in student_data for field in main_fields):
        raise ValueError("Не хватает обязательных полей")
    # формируем параметризованный SQL запрос с подстановкой значений через???
    sql_script = """
    INSERT INTO students (first_name, middle_name, last_name, age, group_id)
    VALUES (?, ?, ?, ?, ?)
    """

    # Извлекаем значения
    values = (
        student_data.get("first_name"),
        student_data.get("middle_name"),
        student_data.get("last_name"),
        student_data.get("age", None),
        student_data.get("group_id", None)
    )

    try:
        cursor.execute(sql_script, values)
        connection.commit()
    except s13.Error as error:
        print(error)
        raise
    finally:
        cursor.close()

new_student = {
    "first_name": "Арагорн",
    "middle_name": "Арахорнович",
    "last_name": "Иванов",
    "age": 50,
    "group_id": 1
}

# добавляем стдуента и выведем таблицу студентов
# create_student(connection, **new_student) # один раз выполнить потом закомитить
# получим данные из таблицы студентов и выведем их
data, columns = get_data_from_table(connection, SQL_SCRIPT1)
print(render_table(data, columns))
# закрываем соединение с базой данных
connection.close()

def execute_query(connection: s13.Connection, sql_query: str, params: tuple) -> tuple|None:
    if "?" not in sql_query:
        raise ValueError("В запросе нет параметров")
    
    if sql_query.count("?") != len(params):
        raise ValueError("Количество параметров не совпадает с количеством вопросов в запросе")
    
    cursor = connection.cursor()
    try:
        cursor.execute(sql_query, params)
        if sql_query.strip().upper().startswith("SELECT"):
            columns = [description[0] for description in cursor.description]
            data = cursor.fetchall()
            return data, columns
        connection.commit()
    except s13.Error as error:
        print(error)
        raise
    finally:
        cursor.close()

sql_script_1 = "SELECT * FROM students WHERE age > ?"
params_1 = (40,)

connection = s13.connect(DB_FILE)
data_1 = execute_query(connection, sql_script_1, params_1)

print(render_table(*data_1))