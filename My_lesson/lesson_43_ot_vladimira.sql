-- Lesson 43 - Система таблиц для Онлайн Академии ТОП и статистике одного преподавателя))
-- Система таблиц для Онлайн Академии ТОП
-- База данных для отслеживания студентов, занятий, домашних заданий и обратной связи
-- SQLite DDL Script
-- Включаем поддержку внешних ключей
PRAGMA foreign_keys = ON;

-- =============================================================================
-- ОСНОВНЫЕ ТАБЛИЦЫ
-- =============================================================================
-- Таблица групп
CREATE TABLE
    groups (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        group_name TEXT NOT NULL UNIQUE,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    );

-- Таблица студентов
CREATE TABLE
    students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        middle_name TEXT,
        last_name TEXT NOT NULL,
        group_id INTEGER NOT NULL,
        notes TEXT,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        -- RESTRICT - удаление группы приведет к ошибке, если есть студенты в этой группе
        FOREIGN KEY (group_id) REFERENCES groups (id) ON DELETE RESTRICT
    );

-- Таблица онлайн занятий в Teams
CREATE TABLE
    online_lessons (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        group_id INTEGER NOT NULL,
        lesson_date DATE DEFAULT (DATE ('now')),
        lesson_time TIME DEFAULT (TIME('now')),
        academic_hours INTEGER DEFAULT 2,
        telegram_record_link TEXT DATEFAULT NULL,
        lesson_theme TEXT NOT NULL,
        lesson_notes TEXT DEFAULT NULL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        -- RESTRICT - удаление группы приведет к ошибке, если есть занятия в этой группе
        FOREIGN KEY (group_id) REFERENCES groups (id) ON DELETE RESTRICT,
        CHECK (
            academic_hours > 0
            AND academic_hours <= 8
        )
    );

-- Таблица для отметки присутствия студентов на занятиях
CREATE TABLE
    students_online_lessons (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER NOT NULL,
        online_lesson_id INTEGER NOT NULL,
        mark INTEGER DEFAULT 6,
        is_active INTEGER DEFAULT 0,
        attendance_notes TEXT,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (student_id) REFERENCES students (id) ON DELETE CASCADE,
        FOREIGN KEY (online_lesson_id) REFERENCES online_lessons (id) ON DELETE CASCADE,
        CHECK (
            mark >= 1
            AND mark <= 12
        ),
        CHECK (is_active IN (0, 1)),
        UNIQUE (student_id, online_lesson_id)
    );

-- =============================================================================
-- ТАБЛИЦЫ ДЛЯ ДОМАШНИХ ЗАДАНИЙ
-- =============================================================================
-- Таблица с текстом выданных домашних заданий
CREATE TABLE
    homeworks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        online_lesson_id INTEGER NOT NULL,
        summary TEXT NOT NULL,
        homework_text TEXT NOT NULL,
        homework_date DATE DEFAULT (DATE ('now')),
        deadline_date DATE DEFAULT (DATE ('now', '+7 days')),
        is_active INTEGER DEFAULT 1,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (online_lesson_id) REFERENCES online_lessons (id) ON DELETE CASCADE,
        CHECK (is_active IN (0, 1)),
        CHECK (deadline_date >= homework_date)
    );

-- Таблица для отметки выполнения домашних заданий (many-to-many)
CREATE TABLE
    homeworks_students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER NOT NULL,
        homework_id INTEGER NOT NULL,
        homework_text TEXT NOT NULL,
        file_path TEXT,
        status TEXT DEFAULT 'отправлено' CHECK (
            status IN (
                'отправлено',
                'на проверке',
                'принято',
                'проверено',
                'на доработку',
                'обратная связь выдана'
            )
        ),
        mark INTEGER,
        submission_date DATETIME DEFAULT CURRENT_TIMESTAMP,
        checked_date DATETIME,
        feedback_text TEXT,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (student_id) REFERENCES students (id) ON DELETE CASCADE,
        FOREIGN KEY (homework_id) REFERENCES homeworks (id) ON DELETE CASCADE,
        CHECK (
            mark IS NULL
            OR (
                mark >= 1
                AND mark <= 12
            )
        ),
        --TODO - Убрать нафиг
        UNIQUE (student_id, homework_id)
    );

-- =============================================================================
-- ТАБЛИЦА ДЛЯ ОБРАТНОЙ СВЯЗИ
-- =============================================================================
-- Таблица для обратной связи на студента
CREATE TABLE
    students_reviews (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER NOT NULL,
        review_text TEXT NOT NULL,
        review_date DATE DEFAULT (DATE ('now')),
        review_start_date DATE,
        review_end_date DATE,
        is_published INTEGER DEFAULT 0,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (student_id) REFERENCES students (id) ON DELETE CASCADE,
        CHECK (is_published IN (0, 1)),
        CHECK (
            review_end_date IS NULL
            OR review_end_date >= review_start_date
        )
    );

-- =============================================================================
-- ИНДЕКСЫ ДЛЯ ОПТИМИЗАЦИИ ЗАПРОСОВ
-- =============================================================================
-- Индексы для частых запросов
CREATE INDEX idx_students_group_id ON students (group_id);

CREATE INDEX idx_students_last_name ON students (last_name);

CREATE INDEX idx_online_lessons_group_id ON online_lessons (group_id);

CREATE INDEX idx_online_lessons_date ON online_lessons (lesson_date);

CREATE INDEX idx_students_online_lessons_student_id ON students_online_lessons (student_id);

CREATE INDEX idx_students_online_lessons_lesson_id ON students_online_lessons (online_lesson_id);

CREATE INDEX idx_homeworks_lesson_id ON homeworks (online_lesson_id);

CREATE INDEX idx_homeworks_deadline ON homeworks (deadline_date);

CREATE INDEX idx_homeworks_students_student_id ON homeworks_students (student_id);

CREATE INDEX idx_homeworks_students_homework_id ON homeworks_students (homework_id);

CREATE INDEX idx_homeworks_students_status ON homeworks_students (status);

CREATE INDEX idx_students_reviews_student_id ON students_reviews (student_id);

CREATE INDEX idx_students_reviews_date ON students_reviews (review_date);

-- =============================================================================
-- ТРИГГЕРЫ ДЛЯ АВТОМАТИЧЕСКОГО ОБНОВЛЕНИЯ ВРЕМЕНИ
-- =============================================================================
-- Триггер для обновления updated_at в таблице groups
CREATE TRIGGER trg_groups_updated_at AFTER
UPDATE ON groups BEGIN
UPDATE groups
SET
    updated_at = CURRENT_TIMESTAMP
WHERE
    id = NEW.id;

END;

-- Триггер для обновления updated_at в таблице students
CREATE TRIGGER trg_students_updated_at AFTER
UPDATE ON students BEGIN
UPDATE students
SET
    updated_at = CURRENT_TIMESTAMP
WHERE
    id = NEW.id;

END;

-- Триггер для обновления updated_at в таблице online_lessons
CREATE TRIGGER trg_online_lessons_updated_at AFTER
UPDATE ON online_lessons BEGIN
UPDATE online_lessons
SET
    updated_at = CURRENT_TIMESTAMP
WHERE
    id = NEW.id;

END;

-- Триггер для обновления updated_at в таблице students_online_lessons
CREATE TRIGGER trg_students_online_lessons_updated_at AFTER
UPDATE ON students_online_lessons BEGIN
UPDATE students_online_lessons
SET
    updated_at = CURRENT_TIMESTAMP
WHERE
    id = NEW.id;

END;

-- Триггер для обновления updated_at в таблице homeworks
CREATE TRIGGER trg_homeworks_updated_at AFTER
UPDATE ON homeworks BEGIN
UPDATE homeworks
SET
    updated_at = CURRENT_TIMESTAMP
WHERE
    id = NEW.id;

END;

-- Триггер для обновления updated_at в таблице homeworks_students
CREATE TRIGGER trg_homeworks_students_updated_at AFTER
UPDATE ON homeworks_students BEGIN
UPDATE homeworks_students
SET
    updated_at = CURRENT_TIMESTAMP
WHERE
    id = NEW.id;

END;

-- Триггер для обновления updated_at в таблице students_reviews
CREATE TRIGGER trg_students_reviews_updated_at AFTER
UPDATE ON students_reviews BEGIN
UPDATE students_reviews
SET
    updated_at = CURRENT_TIMESTAMP
WHERE
    id = NEW.id;

END;

-- Триггер для автоматической установки checked_date при изменении статуса домашки
CREATE TRIGGER trg_homeworks_students_check_date AFTER
UPDATE OF status ON homeworks_students WHEN NEW.status IN (
    'принято',
    'проверено',
    'на доработку',
    'обратная связь выдана'
)
AND OLD.status != NEW.status BEGIN
UPDATE homeworks_students
SET
    checked_date = CURRENT_TIMESTAMP
WHERE
    id = NEW.id
    AND checked_date IS NULL;

END;

-- =============================================================================
-- ПРЕДСТАВЛЕНИЯ ДЛЯ УДОБНЫХ ЗАПРОСОВ
-- =============================================================================
-- Представление для получения полной информации о студентах
CREATE VIEW
    v_students_full AS
SELECT
    s.id,
    s.first_name || ' ' || COALESCE(s.middle_name || ' ', '') || s.last_name AS full_name,
    s.first_name,
    s.middle_name,
    s.last_name,
    g.group_name,
    s.notes,
    s.created_at,
    s.updated_at
FROM
    students s
    JOIN groups g ON s.group_id = g.id;

-- Представление для статистики посещаемости
CREATE VIEW
    v_attendance_stats AS
SELECT
    s.id AS student_id,
    s.first_name || ' ' || s.last_name AS student_name,
    g.group_name,
    COUNT(sol.id) AS total_lessons,
    AVG(CAST(sol.mark AS REAL)) AS avg_mark,
    SUM(sol.is_active) AS active_participation
FROM
    students s
    JOIN groups g ON s.group_id = g.id
    LEFT JOIN students_online_lessons sol ON s.id = sol.student_id
GROUP BY
    s.id,
    s.first_name,
    s.last_name,
    g.group_name;

-- Представление для статистики по домашкам
CREATE VIEW
    v_homework_stats AS
SELECT
    s.id AS student_id,
    s.first_name || ' ' || s.last_name AS student_name,
    g.group_name,
    COUNT(hs.id) AS total_homeworks,
    COUNT(
        CASE
            WHEN hs.status IN ('принято', 'проверено', 'обратная связь выдана') THEN 1
        END
    ) AS completed_homeworks,
    COUNT(
        CASE
            WHEN hs.status = 'не сдано' THEN 1
        END
    ) AS not_submitted,
    AVG(
        CASE
            WHEN hs.mark IS NOT NULL THEN CAST(hs.mark AS REAL)
        END
    ) AS avg_homework_mark
FROM
    students s
    JOIN groups g ON s.group_id = g.id
    LEFT JOIN homeworks_students hs ON s.id = hs.student_id
GROUP BY
    s.id,
    s.first_name,
    s.last_name,
    g.group_name;