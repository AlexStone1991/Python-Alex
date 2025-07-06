from flask import Flask, request, jsonify, abort
from peewee import *
import json
from datetime import datetime
from typing import Dict, List, Optional, Union

app = Flask(__name__)

# Настройка базы данных
db = SqliteDatabase('barbershop_api.db')

# Модель Мастера
class Master(Model):
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    middle_name = CharField(max_length=50, null=True)
    phone = CharField(max_length=20, unique=True)

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

# Функции конвертации
def master_to_dict(master: Master) -> Dict:
    """Преобразует объект Master в словарь"""
    return {
        'id': master.id,
        'first_name': master.first_name,
        'last_name': master.last_name,
        'middle_name': master.middle_name,
        'phone': master.phone
    }

def appointment_to_dict(appointment: Appointment) -> Dict:
    """Преобразует объект Appointment в словарь"""
    return {
        'id': appointment.id,
        'client_name': appointment.client_name,
        'client_phone': appointment.client_phone,
        'date': appointment.date.isoformat(),
        'status': appointment.status,
        'comment': appointment.comment,
        'master': master_to_dict(appointment.master)
    }

# Функции валидации
def validate_master_data(data: Dict) -> None:
    """Проверяет корректность данных для мастера"""
    required_fields = ['first_name', 'last_name', 'phone']
    for field in required_fields:
        if field not in data or not data[field].strip():
            raise ValueError(f'Поле {field} обязательно для заполнения')

    if 'phone' in data and len(data['phone']) < 5:
        raise ValueError('Номер телефона слишком короткий')

def validate_appointment_data(data: Dict) -> None:
    """Проверяет корректность данных для записи"""
    required_fields = ['client_name', 'client_phone', 'master_id']
    for field in required_fields:
        if field not in data or not str(data[field]).strip():
            raise ValueError(f'Поле {field} обязательно для заполнения')

# Обработчики ошибок
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Ресурс не найден'}), 404

@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': str(error)}), 400

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Внутренняя ошибка сервера'}), 500

# Маршруты для мастеров
@app.route('/masters', methods=['GET'])
def get_masters():
    """Получить список всех мастеров"""
    masters = [master_to_dict(master) for master in Master.select()]
    return jsonify({'masters': masters})

@app.route('/masters/<int:master_id>', methods=['GET'])
def get_master(master_id: int):
    """Получить информацию о мастере по ID"""
    try:
        master = Master.get(Master.id == master_id)
        return jsonify(master_to_dict(master))
    except Master.DoesNotExist:
        abort(404)

@app.route('/masters', methods=['POST'])
def create_master():
    """Добавить нового мастера"""
    try:
        data = request.get_json()
        validate_master_data(data)

        master = Master.create(
            first_name=data['first_name'],
            last_name=data['last_name'],
            middle_name=data.get('middle_name'),
            phone=data['phone']
        )

        return jsonify(master_to_dict(master)), 201
    except ValueError as e:
        abort(400, str(e))
    except IntegrityError:
        abort(400, 'Мастер с таким телефоном уже существует')

@app.route('/masters/<int:master_id>', methods=['PUT'])
def update_master(master_id: int):
    """Обновить информацию о мастере"""
    try:
        master = Master.get(Master.id == master_id)
        data = request.get_json()
        validate_master_data(data)

        master.first_name = data['first_name']
        master.last_name = data['last_name']
        master.middle_name = data.get('middle_name')
        master.phone = data['phone']
        master.save()

        return jsonify(master_to_dict(master))
    except Master.DoesNotExist:
        abort(404)
    except ValueError as e:
        abort(400, str(e))
    except IntegrityError:
        abort(400, 'Мастер с таким телефоном уже существует')

@app.route('/masters/<int:master_id>', methods=['DELETE'])
def delete_master(master_id: int):
    """Удалить мастера"""
    try:
        master = Master.get(Master.id == master_id)
        master.delete_instance()
        return '', 204
    except Master.DoesNotExist:
        abort(404)

# Маршруты для записей
@app.route('/appointments', methods=['GET'])
def get_appointments():
    """Получить все записи с опциональной сортировкой"""
    query = Appointment.select()

    # Обработка параметров сортировки
    sort_by = request.args.get('sort_by')
    direction = request.args.get('direction', 'asc')

    if sort_by in ['date', 'status', 'client_name']:
        if direction == 'desc':
            query = query.order_by(getattr(Appointment, sort_by).desc())
        else:
            query = query.order_by(getattr(Appointment, sort_by))

    appointments = [appointment_to_dict(appointment) for appointment in query]
    return jsonify({'appointments': appointments})

@app.route('/appointments/<int:appointment_id>', methods=['GET'])
def get_appointment(appointment_id: int):
    """Получить запись по ID"""
    try:
        appointment = Appointment.get(Appointment.id == appointment_id)
        return jsonify(appointment_to_dict(appointment))
    except Appointment.DoesNotExist:
        abort(404)

@app.route('/appointments/master/<int:master_id>', methods=['GET'])
def get_appointments_by_master(master_id: int):
    """Получить все записи для заданного мастера"""
    try:
        master = Master.get(Master.id == master_id)
        appointments = [appointment_to_dict(appointment)
                      for appointment in Appointment.select()
                      .where(Appointment.master == master)]
        return jsonify({'appointments': appointments})
    except Master.DoesNotExist:
        abort(404)

@app.route('/appointments', methods=['POST'])
def create_appointment():
    """Создать новую запись"""
    try:
        data = request.get_json()
        validate_appointment_data(data)

        appointment = Appointment.create(
            client_name=data['client_name'],
            client_phone=data['client_phone'],
            master=Master.get(Master.id == data['master_id']),
            status=data.get('status', 'ожидает'),
            comment=data.get('comment')
        )

        return jsonify(appointment_to_dict(appointment)), 201
    except ValueError as e:
        abort(400, str(e))
    except Master.DoesNotExist:
        abort(400, 'Указанный мастер не найден')

@app.route('/appointments/<int:appointment_id>', methods=['PUT'])
def update_appointment(appointment_id: int):
    """Обновить запись"""
    try:
        appointment = Appointment.get(Appointment.id == appointment_id)
        data = request.get_json()

        if 'client_name' in data:
            appointment.client_name = data['client_name']
        if 'client_phone' in data:
            appointment.client_phone = data['client_phone']
        if 'master_id' in data:
            appointment.master = Master.get(Master.id == data['master_id'])
        if 'status' in data:
            appointment.status = data['status']
        if 'comment' in data:
            appointment.comment = data['comment']

        appointment.save()
        return jsonify(appointment_to_dict(appointment))
    except Appointment.DoesNotExist:
        abort(404)
    except Master.DoesNotExist:
        abort(400, 'Указанный мастер не найден')

@app.route('/appointments/<int:appointment_id>', methods=['DELETE'])
def delete_appointment(appointment_id: int):
    """Удалить запись"""
    try:
        appointment = Appointment.get(Appointment.id == appointment_id)
        appointment.delete_instance()
        return '', 204
    except Appointment.DoesNotExist:
        abort(404)

if __name__ == '__main__':
    # Создание таблиц при первом запуске
    db.connect()
    db.create_tables([Master, Appointment], safe=True)
    db.close()

    # Запуск приложения
    app.run(debug=True)
