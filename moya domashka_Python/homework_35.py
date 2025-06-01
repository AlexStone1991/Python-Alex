from peewee import *
from datetime import datetime
from typing import List, Optional

# Подключение к базе данных
db = SqliteDatabase('barbershop_ALEX.db')

# Модель Мастера
class Master(Model):
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    middle_name = CharField(max_length=50, null=True)
    phone = CharField(max_length=20, unique=True)

    class Meta:
        database = db

# Модель Услуги
class Service(Model):
    title = CharField(max_length=100, unique=True)
    description = TextField(null=True)
    price = DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        database = db

# Модель Записи
class Appointment(Model):
    client_name = CharField(max_length=100)
    client_phone = CharField(max_length=20)
    date = DateTimeField(default=datetime.now)
    status = CharField(max_length=20, default='ожидает')
    comment = TextField(null=True)
    master = ForeignKeyField(Master, backref='appointments')

    class Meta:
        database = db

# Модель связи Мастер-Услуга
class MasterService(Model):
    master = ForeignKeyField(Master)
    service = ForeignKeyField(Service)

    class Meta:
        database = db
        indexes = (
            (('master', 'service'), True),  # Уникальная пара мастер-услуга
        )

# Модель связи Запись-Услуга
class AppointmentService(Model):
    appointment = ForeignKeyField(Appointment)
    service = ForeignKeyField(Service)

    class Meta:
        database = db
        indexes = (
            (('appointment', 'service'), True),  # Уникальная пара запись-услуга
        )

# Создаем таблицы
def create_tables():
    with db:
        db.create_tables([Master, Service, Appointment, MasterService, AppointmentService])

# Заполняем тестовыми данными
def populate_database():
    # Создаем мастеров
    ivan = Master.create(first_name='Иван', last_name='Иванов', middle_name='Иванович', phone='123-456-7890')
    anna = Master.create(first_name='Анна', last_name='Петрова', middle_name='Сергеевна', phone='987-654-3210')

    # Создаем услуги
    haircut = Service.create(title='Стрижка', description='Классическая стрижка', price=1000)
    shaving = Service.create(title='Бритье', description='Классическое бритье', price=800)
    styling = Service.create(title='Укладка', description='Укладка волос', price=1200)
    coloring = Service.create(title='Окрашивание', description='Окрашивание волос', price=1500)
    manicure = Service.create(title='Маникюр', description='Маникюр для мужчин', price=700)

    # Связываем мастеров с услугами
    MasterService.create(master=ivan, service=haircut)
    MasterService.create(master=ivan, service=shaving)
    MasterService.create(master=anna, service=styling)
    MasterService.create(master=anna, service=coloring)
    MasterService.create(master=ivan, service=manicure)

    # Создаем записи
    alexey = Appointment.create(
        client_name='Алексей',
        client_phone='111-222-3333',
        master=ivan,
        status='подтверждена',
        comment='Хочет короткую стрижку'
    )
    AppointmentService.create(appointment=alexey, service=haircut)
    AppointmentService.create(appointment=alexey, service=shaving)

    boris = Appointment.create(
        client_name='Борис',
        client_phone='444-555-6666',
        master=anna,
        status='подтверждена',
        comment='Укладка на свадьбу'
    )
    AppointmentService.create(appointment=boris, service=styling)

    viktor = Appointment.create(
        client_name='Виктор',
        client_phone='777-888-9999',
        master=ivan,
        status='ожидает',
        comment='Бритье и стрижка'
    )
    AppointmentService.create(appointment=viktor, service=coloring)

# Выводим данные в консоль
def print_database_contents():
    print("\nМастера:")
    for master in Master.select():
        print(f"{master.id}. {master.first_name} {master.last_name} {master.middle_name}, телефон: {master.phone}")

    print("\nУслуги:")
    for service in Service.select():
        print(f"{service.id}. {service.title} - {service.description}, цена: {service.price}")

    print("\nЗаписи:")
    for appointment in Appointment.select():
        master_name = f"{appointment.master.first_name} {appointment.master.last_name}"
        services = [aservice.service.title for aservice in AppointmentService.select().where(AppointmentService.appointment == appointment)]
        print(f"{appointment.id}. Клиент: {appointment.client_name}, телефон: {appointment.client_phone}")
        print(f"   Мастер: {master_name}, статус: {appointment.status}")
        print(f"   Услуги: {', '.join(services)}")
        print(f"   Комментарий: {appointment.comment}")
        print("---")

def main():
    create_tables()
    populate_database()
    print_database_contents()

if __name__ == '__main__':
    main()
