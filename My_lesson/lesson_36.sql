-- SQL Ч2. Подзапросы. Знакомство с GROUP BY. Урок 36.
-- получили уникальные значения по цвету волос
SELECT DISTINCT HAIR
FROM MarvelCharacters;

-- вроде бы тоже самое но бд будет хранить данные о каждом уникальном значении(соберет группы)
SELECT HAIR
FROM MarvelCharacters
GROUP BY HAIR;

-- функция COUNT() - считает количество строк в таблице
SELECT COUNT(*)
FROM MarvelCharacters;

-- уникальные цвета волос
SELECT COUNT(DISTINCT HAIR) 
FROM MarvelCharacters;

-- колличество лысых персонажей
SELECT COUNT(*) 
FROM MarvelCharacters
WHERE HAIR = 'Bald';

-- подсчет колличетвва строк в табюлице гд есть значения в столбце HAIR
SELECT COUNT(HAIR)
FROM MarvelCharacters;

-- вывод названия и подсчет лысых персонажей
SELECT HAIR, COUNT(HAIR)
FROM MarvelCharacters
WHERE HAIR = 'Bald';

-- первый запрос с группировкой считаем сколько персонажей с каждым цветом волос
SELECT HAIR, COUNT(*)
FROM MarvelCharacters
GROUP BY HAIR
ORDER BY COUNT(*) DESC;

-- считаем сколько персонажей с каждым цветом волос, но только тех у кого есть значение с этом столбце
SELECT HAIR, COUNT(*) AS hair_count
FROM MarvelCharacters
WHERE HAIR IS NOT NULL
GROUP BY HAIR
ORDER BY hair_count DESC;

-- подсчет колличества персонажей с каждым цветом глаз
SELECT EYE, COUNT(*) AS eye_count
FROM MarvelCharacters
WHERE EYE IS NOT NULL
GROUP BY EYE
ORDER BY eye_count DESC;

-- SUM сумма значений в столбце
-- группировка по цвету глаз подсчет кол ва персонажей а так же суммы APPEARANCES

SELECT EYE, COUNT(*) AS eye_count, SUM(APPEARANCES) AS total_appearances
FROM MarvelCharacters
WHERE EYE IS NOT NULL
GROUP BY EYE
ORDER BY total_appearances DESC;

SELECT Year, COUNT(*) AS character_count
FROM MarvelCharacters
WHERE Year IS NOT NULL
GROUP BY Year
ORDER BY Year;

-- avg() - вычесляет среднее значение
-- count() - подсчитывает колличество строк или значений
-- group_concat() - объединяет значения в одну строку
-- max() - находит максимальное значение
-- min() - находит минимальное значение
-- sum() - вычисляет сумму значений
-- total() - аналогичный sum(), но преобразует целые числа в вещественные

SELECT year, COUNT(*) AS year_count, MAX(APPEARANCES) AS max_appearances, AVG(APPEARANCES) AS avg_appearances, SUM(APPEARANCES) AS total_appearances
FROM MarvelCharacters
GROUP BY year;

-- сделайте группировку по indentify посчитайте количество персонаже
-- сделайте группировку по Alive посчитайте количество персонажей сделайте сортировку по количеству персонажей

SELECT identify, COUNT(*) AS identify_count
FROM MarvelCharacters
WHERE identify IS NOT NULL
GROUP BY identify
ORDER BY identify_count DESC;

SELECT ALIVE, COUNT(*) AS alive_count
FROM MarvelCharacters
WHERE ALIVE IS NOT NULL
GROUP BY ALIVE
ORDER BY alive_count DESC;


-- ПОДЗАПРОСЫ
-- это возможность сделать запрос внутри запроса
SELECT name, APPEARANCES
FROM MarvelCharacters
WHERE APPEARANCES > AVG(APPEARANCES)
ORDER BY APPEARANCES DESC;

SELECT name, APPEARANCES
FROM MarvelCharacters
WHERE APPEARANCES > (
    SELECT AVG(APPEARANCES) 
    FROM MarvelCharacters
)
ORDER BY APPEARANCES DESC;

-- CTE - Common Table Expression
-- это возможность сделать запрос внутри запроса, но более читабельно

WITH AverageAppearances AS (
    SELECT AVG(APPEARANCES) AS avg_appearances
    FROM MarvelCharacters
)
SELECT name, APPEARANCES
FROM MarvelCharacters, AverageAppearances
WHERE APPEARANCES > avg_appearances
ORDER BY APPEARANCES DESC;


-- =================Marvel Normal==================

SELECT name, eye_id
FROM MarvelCharacters;

SELECT eye_id, color
FROM EyeColor
WHERE eye_id = 1;

SELECT name, color
FROM MarvelCharacters
JOIN EyeColor ON MarvelCharacters.eye_id = EyeColor.eye_id;