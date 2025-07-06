from peewee import *
from playhouse.signals import post_save
from datetime import datetime
from typing import List, Optional

# Подключение к базе данных
db = SqliteDatabase('barbershop.db')

class BaseModel(Model):
    class Meta:
        database = db

# Модель Мастера
class Master(BaseModel):
    first_name = CharField(max_length=50, verbose_name='Имя')
    last_name = CharField(max_length=50, verbose_name='Фамилия')
    middle_name = CharField(max_length=50, null=True, verbose_name='Отчество')
    phone = CharField(max_length=20, unique=True, verbose_name='Телефон')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Модель Услуги
class Service(BaseModel):
    title = CharField(max_length=100, unique=True, verbose_name='Название')
    description = TextField(null=True, verbose_name='Описание')
    price = DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return self.title

# Модель Записи
class Appointment(BaseModel):
    client_name = CharField(max_length=100, verbose_name='Имя клиента')
    client_phone = CharField(max_length=20, verbose_name='Телефон клиента')
    date = DateTimeField(default=datetime.now, verbose_name='Дата записи')
    status = CharField(max_length=20, default='ожидает', verbose_name='Статус')
    comment = TextField(null=True, verbose_name='Комментарий')
    master = ForeignKeyField(Master, backref='appointments', verbose_name='Мастер')

    def validate(self):
        """Валидация данных записи."""
        if not self.client_name.strip():
            raise ValidationError("Имя клиента не может быть пустым")
        if not self.client_phone.strip():
            raise ValidationError("Телефон клиента не может быть пустым")
        if len(self.client_phone) < 5:
            raise ValidationError("Телефон слишком короткий")

    def __str__(self):
        return f"Запись #{self.id} для {self.client_name}"

# Модель связи Мастер-Услуга
class MasterService(BaseModel):
    master = ForeignKeyField(Master, verbose_name='Мастер')
    service = ForeignKeyField(Service, verbose_name='Услуга')

    class Meta:
        indexes = (
            (('master', 'service'), True),  # Уникальная пара мастер-услуга
        )

# Модель связи Запись-Услуга
class AppointmentService(BaseModel):
    appointment = ForeignKeyField(Appointment, verbose_name='Запись')
    service = ForeignKeyField(Service, verbose_name='Услуга')

    class Meta:
        indexes = (
            (('appointment', 'service'), True),  # Уникальная пара запись-услуга
        )

# Сигнал для валидации перед сохранением записи
@post_save(sender=Appointment)
def validate_appointment(model_class, instance, created):
    try:
        instance.validate()
    except ValidationError as e:
        if created:  # Если это новая запись
            instance.delete_instance()  # Удаляем невалидную запись
        raise e

def initialize_database():
    """Инициализирует базу данных."""
    db.connect()
    db.create_tables([
        Master,
        Service,
        Appointment,
        MasterService,
        AppointmentService
    ], safe=True)

def populate_initial_data():
    """Заполняет базу начальными данными."""
    if Master.select().count() == 0:  # Проверяем, пустая ли база
        # Создаем мастеров
        masters_data = [
            {'first_name': 'Иван', 'last_name': 'Иванов', 'phone': '123-456-7890'},
            {'first_name': 'Анна', 'last_name': 'Петрова', 'phone': '987-654-3210'}
        ]

        masters = [Master.create(**data) for data in masters_data]

        # Создаем услуги
        services_data = [
            {'title': 'Стрижка', 'description': 'Классическая стрижка', 'price': 1000.00},
            {'title': 'Бритье', 'description': 'Классическое бритье', 'price': 800.00},
            {'title': 'Укладка', 'description': 'Укладка волос', 'price': 1200.00},
            {'title': 'Окрашивание', 'description': 'Окрашивание волос', 'price': 1500.00},
            {'title': 'Маникюр', 'description': 'Маникюр для мужчин', 'price': 700.00}
        ]

        services = [Service.create(**data) for data in services_data]

        # Связываем мастеров с услугами
        master_services = [
            (masters[0], services[0]), (masters[0], services[1]),  # Иван: Стрижка, Бритье
            (masters[1], services[2]), (masters[1], services[3]),  # Анна: Укладка, Окрашивание
            (masters[0], services[4])   # Иван: Маникюр
        ]

        for master, service in master_services:
            MasterService.create(master=master, service=service)

def create_appointment(client_name: str, client_phone: str, master_name: str,
                     services: List[str], comment: Optional[str] = None) -> int:
    """Создает новую запись с проверками."""
    try:
        # Проверяем существование мастера
        master = Master.get((Master.first_name == master_name.split()[0]) &
                          (Master.last_name == master_name.split()[1]))

        # Проверяем существование услуг
        service_objects = []
        for service_title in services:
            try:
                service = Service.get(Service.title == service_title)
                service_objects.append(service)
            except Service.DoesNotExist:
                raise ValueError(f"Услуга '{service_title}' не найдена")

        # Создаем запись
        with db.atomic():
            appointment = Appointment.create(
                client_name=client_name,
                client_phone=client_phone,
                master=master,
                status='ожидает',
                comment=comment
            )

            # Связываем услуги
            for service in service_objects:
                AppointmentService.create(
                    appointment=appointment,
                    service=service
                )

        return appointment.id

    except Master.DoesNotExist:
        raise ValueError(f"Мастер '{master_name}' не найден")

def print_database_contents():
    """Выводит содержимое базы данных в удобном формате."""
    print("\n=== Мастера ===")
    for master in Master.select():
        print(f"{master.id}. {master.first_name} {master.last_name} ({master.phone})")

    print("\n=== Услуги ===")
    for service in Service.select():
        print(f"{service.id}. {service.title} - {service.price} руб. ({service.description})")

    print("\n=== Записи ===")
    for appointment in Appointment.select():
        services = [aservice.service.title for aservice in
                   AppointmentService.select().where(AppointmentService.appointment == appointment)]

        print(f"\nЗапись #{appointment.id}")
        print(f"Клиент: {appointment.client_name} ({appointment.client_phone})")
        print(f"Мастер: {appointment.master}")
        print(f"Дата: {appointment.date}")
        print(f"Статус: {appointment.status}")
        print(f"Услуги: {', '.join(services)}")
        if appointment.comment:
            print(f"Комментарий: {appointment.comment}")
        print("-" * 40)

def main():
    """Основная функция программы."""
    initialize_database()
    populate_initial_data()

    # Пример создания новой записи
    try:
        new_appointment_id = create_appointment(
            client_name='Дмитрий',
            client_phone='555-666-7777',
            master_name='Иван Иванов',
            services=['Стрижка', 'Бритье'],
            comment='Новая запись'
        )
        print(f"\nСоздана новая запись с ID: {new_appointment_id}")
    except Exception as e:
        print(f"\nОшибка при создании записи: {e}")

    # Выводим содержимое базы
    print_database_contents()

if __name__ == '__main__':
    main()
