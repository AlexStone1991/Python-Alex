import sqlite3
from typing import List, Tuple, Optional

# Константы
DB_PATH = r"C:/ALEXXX/Python-Alex/Data/barbershop.db"
SQL_FILE_PATH = r"C:/ALEXXX/Python-Alex/moya domashka_Python/domashka_33_barbershop.sql"

def read_sql_file(filepath: str) -> str:
    """Читает текст SQL-скрипта из файла и возвращает его содержимое."""
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def execute_script(conn: sqlite3.Connection, script: str) -> None:
    """Выполняет SQL-скрипт через соединение."""
    cursor = conn.cursor()
    cursor.executescript(script)
    conn.commit()

def find_appointment_by_phone(conn: sqlite3.Connection, phone: str) -> List[Tuple]:
    """Ищет записи по номеру телефона."""
    query = """
    SELECT a.id, a.name, a.phone, a.date, a.status, a.comment,
           m.first_name || ' ' || m.last_name AS master_name,
           GROUP_CONCAT(s.title, ', ') AS services
    FROM appointments a
    JOIN masters m ON a.master_id = m.id
    JOIN appointments_services asv ON a.id = asv.appointment_id
    JOIN services s ON asv.service_id = s.id
    WHERE a.phone = ?
    GROUP BY a.id
    """
    cursor = conn.cursor()
    cursor.execute(query, (phone,))
    return cursor.fetchall()

def find_appointment_by_comment(conn: sqlite3.Connection, comment_part: str) -> List[Tuple]:
    """Ищет записи по части комментария."""
    query = """
    SELECT a.id, a.name, a.phone, a.date, a.status, a.comment,
           m.first_name || ' ' || m.last_name AS master_name,
           GROUP_CONCAT(s.title, ', ') AS services
    FROM appointments a
    JOIN masters m ON a.master_id = m.id
    JOIN appointments_services asv ON a.id = asv.appointment_id
    JOIN services s ON asv.service_id = s.id
    WHERE a.comment LIKE ?
    GROUP BY a.id
    """
    cursor = conn.cursor()
    cursor.execute(query, (f'%{comment_part}%',))
    return cursor.fetchall()

def create_appointment(conn: sqlite3.Connection, client_name: str, client_phone: str,
                     master_name: str, services_list: List[str], comment: Optional[str] = None) -> int:
    """Создает новую запись в базе данных."""
    # Получаем ID мастера
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM masters WHERE first_name || ' ' || last_name = ?", (master_name,))
    master_id = cursor.fetchone()[0]

    # Создаем запись
    cursor.execute(
        "INSERT INTO appointments (name, phone, master_id, status, comment) VALUES (?, ?, ?, 'ожидает', ?)",
        (client_name, client_phone, master_id, comment)
    )
    appointment_id = cursor.lastrowid

    # Связываем услуги
    for service_title in services_list:
        cursor.execute("SELECT id FROM services WHERE title = ?", (service_title,))
        service_id = cursor.fetchone()[0]
        cursor.execute(
            "INSERT INTO appointments_services (appointment_id, service_id) VALUES (?, ?)",
            (appointment_id, service_id)
        )

    conn.commit()
    return appointment_id

def main():
    # Создаем соединение с базой данных
    conn = sqlite3.connect(DB_PATH)

    # Создаем таблицы и заполняем тестовыми данными
    sql_script = read_sql_file(SQL_FILE_PATH)
    execute_script(conn, sql_script)

    # Тестируем функции
    print("Поиск по телефону '111-222-3333':")
    appointments = find_appointment_by_phone(conn, '111-222-3333')
    for appointment in appointments:
        print(appointment)

    print("\nПоиск по комментарию 'стриж':")
    appointments = find_appointment_by_comment(conn, 'стриж')
    for appointment in appointments:
        print(appointment)

    print("\nСоздание новой записи:")
    new_appointment_id = create_appointment(
        conn,
        'Дмитрий',
        '555-666-7777',
        'Иван Иванов',
        ['Стрижка', 'Бритье'],
        'Новая запись'
    )
    print(f"Создана запись с ID: {new_appointment_id}")

    # Закрываем соединение
    conn.close()

if __name__ == "__main__":
    main()
