-- Lesson 39 - Создание собственной системы таблиц 
-- Students - Таблица студентов
-- Groups - Таблица групп
-- Teachers - Таблица преподавателей
-- TeacherGroups - Таблица групп преподавателей
-- StudentsCards - Таблица студенческих карточек

-- 1. Таблица групп студентов
CREATE TABLE
    IF NOT EXISTS Groups (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        group_name TEXT NOT NULL UNIQUE,
        start_date DATE DEFAULT CURRENT_TIMESTAMP,
        end_date DATE
    );

-- 2. Таблица студентов
CREATE TABLE
    IF NOT EXISTS Students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        middle_name TEXT,
        last_name TEXT NOT NULL,
        age INTEGER DEFAULT 0,
        group_id INTEGER DEFAULT NULL,
        FOREIGN KEY (group_id) REFERENCES Groups (id) ON DELETE SET DEFAULT ON UPDATE CASCADE
    );

-- Индекс для group_id
CREATE INDEX IF NOT EXISTS idx_group_id ON Students (group_id);

-- Индекс для фамилии
CREATE INDEX IF NOT EXISTS idx_last_name ON Students (last_name);

-- Составной индекс для ФИО
CREATE INDEX IF NOT EXISTS idx_full_name ON Students (first_name, last_name, middle_name);


CREATE TABLE IF NOT EXISTS StudentsCards (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    card_number TEXT UNIQUE,
    card_status TEXT DEFAULT 'active',
    notes TEXT DEFAULT NULL,
    created_date DATE DEFAULT CURRENT_TIMESTAMP,
    issued_date DATE DEFAULT Null,
    FOREIGN KEY (student_id) REFERENCES Students (id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Индекс для внешнего ключа
CREATE INDEX IF NOT EXISTS idx_student_id ON StudentsCards (student_id);

-- 3. Добавление групп в БД
INSERT INTO
    Groups (group_name)
VALUES
    ('python411'),
    ('python412'),
    ('python413');

INSERT INTO Students (first_name, middle_name, last_name, age, group_id)
VALUES 
('Светозара', 'Питоновна', 'Джангова', 20, (SELECT id FROM Groups WHERE group_name = 'python412')),
('Кодислав', 'Гитович', 'Коммитов', 21, (SELECT id FROM Groups WHERE group_name = 'python412')),
('Серверина', 'Базоданных', 'Селектова', 22, (SELECT id FROM Groups WHERE group_name = 'python412')),
('Фронтендий', 'Вебович', 'Реактов', 23, (SELECT id FROM Groups WHERE group_name = 'python412')),
('Линуксина', 'Убунтовна', 'Баширова', 24, (SELECT id FROM Groups WHERE group_name = 'python412')),
('Алгоритм', 'Сортирович', 'Рекурсионов', 23, (SELECT id FROM Groups WHERE group_name = 'python413')),
('Нейросеть', 'Вижновна', 'Трансформерова', 23, (SELECT id FROM Groups WHERE group_name = 'python413')),
('Блокчейн', 'Криптович', 'Токенов', 23, (SELECT id FROM Groups WHERE group_name = 'python413')),
('Явана', 'Скриптовна', 'Ноутация', 23, (SELECT id FROM Groups WHERE group_name = 'python413')),
('Облакос', 'Докерович', 'Кубернетов', 23, (SELECT id FROM Groups WHERE group_name = 'python413'));

-- Таблица преподавателей
CREATE TABLE IF NOT EXISTS Teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    middle_name TEXT,
    last_name TEXT NOT NULL,
    age INTEGER DEFAULT 0,
    email TEXT DEFAULT NULL,
    phone TEXT
);

-- Индексы преподов по телефону, фамилии, ФИО
CREATE INDEX IF NOT EXISTS idx_teacher_phone ON Teachers (phone);
CREATE INDEX IF NOT EXISTS idx_teacher_last_name ON Teachers (last_name);
CREATE INDEX IF NOT EXISTS idx_teacher_full_name ON Teachers (first_name, last_name, middle_name);


-- Создаем преподавателей
INSERT INTO Teachers (first_name, last_name, phone)
VALUES
('Джанго', 'Деплойный', '+79951552295'),
('Фласк', 'Микросервисный', '8-777-343-43-33'),
('Питонья', 'Строкова', '7-333-443-33-44'),
('Семён', 'Кубернетов', '8-333-232-32-23');


CREATE TABLE IF NOT EXISTS TeacherGroups (
    teacher_id INTEGER DEFAULT NULL,
    group_id INTEGER DEFAULT NULL,
    start_date DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (teacher_id) REFERENCES Teachers (id) ON DELETE SET DEFAULT ON UPDATE CASCADE,
    FOREIGN KEY (group_id) REFERENCES Groups (id) ON DELETE SET DEFAULT ON UPDATE CASCADE
    PRIMARY KEY (teacher_id, group_id) -- Автоматическая проверка уникальности пары
);

-- Два отдельных индекса для teacher_id и group_id
CREATE INDEX IF NOT EXISTS idx_teacher_id ON TeacherGroups (teacher_id);
CREATE INDEX IF NOT EXISTS idx_group_id ON TeacherGroups (group_id);

-- Назначение преподавателей на группы
-- Вариант где мы просто укажем ID Назначим препод 1 в группу 3
INSERT INTO TeacherGroups (teacher_id, group_id)
VALUES 
    (1, 3),
    (2, 1),
    (3, 2),
    (4, 3);

-- Микросервисный в группу python413
INSERT INTO TeacherGroups (teacher_id, group_id)
VALUES (
    -- Ищем препода по фамилии
    (SELECT id FROM Teachers WHERE last_name = 'Микросервисный' LIMIT 1),
    -- Ищем группу по имени
    (SELECT id FROM Groups WHERE group_name = 'python413' LIMIT 1)
);

-- Внесем студента БЕЗ группы
INSERT INTO Students (first_name, last_name, age)
VALUES ('Данила', 'Поперечный', 30);