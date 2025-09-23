-- Отключение проверки внешних ключей
PRAGMA foreign_keys = OFF;

-- Начало транзакции
BEGIN TRANSACTION;

-- Создание таблицы "Запись на услуги"
CREATE TABLE IF NOT EXISTS appointments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT NOT NULL,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    master_id INTEGER,
    status TEXT NOT NULL,
    comment TEXT,
    FOREIGN KEY (master_id) REFERENCES masters(id)
);

-- Создание таблицы "Мастера"
CREATE TABLE IF NOT EXISTS masters (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    middle_name TEXT,
    phone TEXT NOT NULL
);

-- Создание таблицы "Услуги"
CREATE TABLE IF NOT EXISTS services (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL UNIQUE,
    description TEXT,
    price REAL NOT NULL
);

-- Создание связующей таблицы "masters_services"
CREATE TABLE IF NOT EXISTS masters_services (
    master_id INTEGER,
    service_id INTEGER,
    PRIMARY KEY (master_id, service_id),
    FOREIGN KEY (master_id) REFERENCES masters(id),
    FOREIGN KEY (service_id) REFERENCES services(id)
);

-- Создание связующей таблицы "appointments_services"
CREATE TABLE IF NOT EXISTS appointments_services (
    appointment_id INTEGER,
    service_id INTEGER,
    PRIMARY KEY (appointment_id, service_id),
    FOREIGN KEY (appointment_id) REFERENCES appointments(id),
    FOREIGN KEY (service_id) REFERENCES services(id)
);

-- Добавление данных о мастерах
INSERT INTO masters (first_name, last_name, middle_name, phone) VALUES
('Иван', 'Иванов', 'Иванович', '123-456-7890'),
('Анна', 'Петрова', 'Сергеевна', '987-654-3210');

-- Добавление данных об услугах
INSERT INTO services (title, description, price) VALUES
('Стрижка', 'Классическая стрижка', 1000),
('Бритье', 'Классическое бритье', 800),
('Укладка', 'Укладка волос', 1200),
('Окрашивание', 'Окрашивание волос', 1500),
('Маникюр', 'Маникюр для мужчин', 700);

-- Связывание мастеров и услуг
INSERT INTO masters_services (master_id, service_id) VALUES
(1, 1), -- Иван Иванов оказывает услугу "Стрижка"
(1, 2), -- Иван Иванов оказывает услугу "Бритье"
(2, 3), -- Анна Петрова оказывает услугу "Укладка"
(2, 4), -- Анна Петрова оказывает услугу "Окрашивание"
(1, 5); -- Иван Иванов оказывает услугу "Маникюр"

-- Добавление записей на услуги
INSERT INTO appointments (name, phone, master_id, status, comment) VALUES
('Алексей', '111-222-3333', 1, 'подтверждена', 'Хочет короткую стрижку'),
('Борис', '444-555-6666', 2, 'подтверждена', 'Укладка на свадьбу'),
('Виктор', '777-888-9999', 1, 'ожидает', 'Бритье и стрижка'),
('Геннадий', '222-333-4444', 2, 'отменена', 'Передумал');

-- Связывание записей и услуг
INSERT INTO appointments_services (appointment_id, service_id) VALUES
(1, 1), -- Алексей записался на "Стрижка"
(1, 2), -- Алексей записался на "Бритье"
(2, 3), -- Борис записался на "Укладка"
(3, 4), -- Виктор записался на "Окрашивание"
(4, 5); -- Геннадий записался на "Маникюр"

-- Добавление индексов
-- Индекс на поле phone в таблице appointments для ускорения поиска по номеру телефона
CREATE INDEX idx_appointments_phone ON appointments(phone);

-- Индекс на поле master_id в таблице appointments для ускорения поиска по мастеру
CREATE INDEX idx_appointments_master_id ON appointments(master_id);

-- Составной индекс на поля master_id и service_id в таблице masters_services
CREATE INDEX idx_masters_services ON masters_services(master_id, service_id);

-- Составной индекс на поля appointment_id и service_id в таблице appointments_services
CREATE INDEX idx_appointments_services ON appointments_services(appointment_id, service_id);

-- Завершение транзакции
COMMIT;

-- Включение проверки внешних ключей
PRAGMA foreign_keys = ON;
