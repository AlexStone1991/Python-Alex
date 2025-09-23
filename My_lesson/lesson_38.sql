-- TODO Тема SQL. Ч4. CRUD. Создание собственной Базы Данных. Урок 38

-- Students - таблица студентов
-- Groups - таблица групп
-- Teachers - таблица преподавателей
-- TeacherGroups - таблица групп преподавателе
-- StudentCards - Taблица студенчиких карточек

-- Students
CREATE TABLE IF NOT EXISTS  Students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    middle_name TEXT,
    last_name TEXT NOT NULL,
    age INTEGER DEFAULT 0,
    group_name TEXT NOT NULL
);

-- Внесем студентов в таблицу
-- Светозара Питоновна Джангова - девушка, которая обожает Python и фреймворк Django.
-- Кодислав Гитович Коммитов - студент, который всегда держит свой код в идеальном порядке с помощью Git.
-- Серверина Базоданных Селектова - молодая девушка с удивительными навыками в SQL-запросах.
-- Фронтендий Вебович Реактов - парень, который предпочитает работать с интерфейсами и React.
-- Линуксина Убунтовна Баширова - студентка, влюбленная в операционные системы на базе Linux и Bash-скрипты.
-- Алгоритм Сортирович Рекурсионов - талантливый студент, который может оптимизировать любой код.
-- Нейросеть Вижновна Трансформерова - дама, увлечённая искусственным интеллектом и компьютерным зрением.
-- Блокчейн Криптович Токенов - студент, который постоянно рассказывает о перспективах децентрализованных систем.
-- Явана Скриптовна Ноутация - девушка, одинаково хорошо владеющая и Java, и JavaScript.
-- Облакос Докерович Кубернетов - молодой человек, фанатеющий от облачных технологий и контейнеризации.

-- добалвяем одного студента в БД
INSERT INTO Students (first_name, last_name, group_name) VALUES ('Филипп', 'Киркоров', 'Python413');
INSERT INTO Students (first_name, middle_name, last_name, age, group_name) VALUES ('Алексей', 'Михайлович', 'Лапшин', 34, 'Python413');

INSERT INTO Students (first_name, middle_name, last_name, age, group_name) VALUES ('Светозара', 'Питоновна', 'Джангова', 20, 'Python413'), ('Кодислав', 'Гитович', 'Коммитов', 22, 'Python413'), ('Серверина', 'Базоданных', 'Селектова', 19, 'Python413'), ('Фронтендий', 'Вебович', 'Реактов', 21, 'Python413'), ('Линуксина', 'Убунтовна', 'Баширова', 20, 'Python413'),
-- еще 5 студентов
('Алгоритм', 'Сортирович', 'Рекурсионов', 23, 'Python413'), ('Нейросеть', 'Вижновна', 'Трансформерова', 22, 'Python413'), ('Блокчейн', 'Криптович', 'Токенов', 21, 'Python413'), ('Явана', 'Скриптовна', 'Ноутация', 20, 'Python413'), ('Облакос', 'Докерович', 'Кубернетов', 23, 'Python413');

-- удалим лишнего студента из группы Python413

-- DELETE FROM Students
-- WHERE first_name = 'Филипп' AND last_name = 'Киркоров' AND group_name = 'Python413';

DELETE FROM Students
WHERE id = (SELECT id 
            FROM Students 
            WHERE first_name = 'Филипп' 
                AND last_name = 'Киркоров' 
                AND group_name = 'Python413' 
            LIMIT 1);

-- удаляем по вхожджению по id
DELETE FROM Students
WHERE id IN (18);

-- обновим данные студента id 1
UPDATE Students
SET middle_name = 'Бедросович', age = 45
WHERE id = 2;

-- Создание таблицы GROUPS

CREATE TABLE IF NOT EXISTS Groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    group_name TEXT NOT NULL UNIQUE,
    -- дата время по умолчанию
    start_data DATA DEFAULT CURRENT_TIMESTAMP,
    end_data DATE
);

-- созданим группы в бд

INSERT INTO Groups (group_name) 
VALUES
('Python411'),
('Python412'),
('Python413');

-- Нормализация таблица студентов
--  так как SQLLITE не поддерживает переименование и удаление столбцов, нам нужно
-- 1. Создать таблицу StudentsNew с нужными столбцами
-- 2. Убедиться что все группы Students есть в Groups
-- 3. Перенести данные из Students в StudentsNew
-- 4. Удалить таблицу Students
-- 5. Переименовать таблицу StudentsNew в Students

CREATE TABLE IF NOT EXISTS StudentsNew (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    middle_name TEXT,
    last_name TEXT NOT NULL,
    age INTEGER DEFAULT 0,
    group_id INTEGER NOT NULL,
    FOREIGN KEY (group_id) REFERENCES Groups(id)
);

INSERT INTO StudentsNew (id, first_name, middle_name, last_name, age, group_id)
SELECT s.id, s.first_name, s.middle_name, s.last_name, s.age, g.id
FROM Students AS s
JOIN Groups AS g ON s.group_name = g.group_name;

-- как удалить таблицу
DROP TABLE IF EXISTS StudentsNew;
DROP TABLE IF EXISTS Students;
DROP TABLE IF EXISTS Groups;


ALTER TABLE StudentsNew RENAME TO Students;

