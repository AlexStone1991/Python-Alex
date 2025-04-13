-- # TODO Тема SQL. Ч1. Установка софта. Первые SELECT. Урок 35.

SELECT *
FROM MarvelCharacters;

-- SQL - декларативный язык, мы описываем то, что хотим получить, а не как это сделать

-- SELECT - выбираем данные из таблицы
-- FROM - из какой таблицы
-- WHERE - фильтруем данные по определённому условию
-- ORDER BY - сортируем данные по определённому полю
-- LIMIT - ограничиваем количество возвращаемых строк
-- OFFSET - пропускаем определённое количество строк
-- DISTINCT - выбираем только уникальные значения

SELECT name, EYE, HAIR, SEX, Appearances
FROM MarvelCharacters
WHERE APPEARANCES > 1000
ORDER BY APPEARANCES DESC;

-- В WHERE доступны булевы выражения, как в Python
-- >, <, >=, <=, !=, =
-- AND, OR, NOT
-- BETWEEN - между двумя значениями
-- IN - в списке значений
-- LIKE - по шаблону
-- IS NULL - проверка на NULL

SELECT name, APPEARANCES
FROM MarvelCharacters
WHERE HAIR = 'Bald' AND APPEARANCES > 10
ORDER BY APPEARANCES DESC;

-- Строки для поиска обязательно в одиночных кавычках ''
-- Названия столбцов, псевдонимы, названия таблиц можно в двойных кавычках
-- Регистрозависимость для поиска, но не для названия столбцов и таблиц

-- DISTINCT - выбираем только уникальные значения
SELECT DISTINCT HAIR
FROM MarvelCharacters;

SELECT DISTINCT EYE
FROM MarvelCharacters;

SELECT DISTINCT EYE, HAIR
FROM MarvelCharacters
WHERE EYE IS NOT NULL AND HAIR IS NOT NULL;
-- NULL - это не значение, а отсутствие значения


--PRACTICE Добудьте уникальные значения по полу SEX
-- Выберите интересное вам значение, и найдите всех персонажей этим полом
SELECT DISTINCT SEX
FROM MarvelCharacters;

SELECT name, APPEARANCES, year, SEX
FROM MarvelCharacters
WHERE SEX = 'Genderfluid Characters' OR SEX = 'Agender Characters'
ORDER BY APPEARANCES DESC;

SELECT *
FROM MarvelCharacters
WHERE year IS NOT NULL
ORDER BY year DESC;

-- Персонажи с 39 по 45
SELECT * FROM MarvelCharacters 
WHERE 
    year IS NOT NULL
    AND year > 1939
    AND year < 1946;

-- Вариант 2. BEETWEEN - мы можем указать диапазон значений
SELECT * FROM MarvelCharacters 
WHERE 
    year IS NOT NULL
    AND year BETWEEN 1939 AND 1945;

-- IN - вхождение в список значений
SELECT * FROM MarvelCharacters 
WHERE 
    year IS NOT NULL
    AND year IN (1939, 1940, 1941, 1942, 1943, 1944, 1945);

-- Ищем "злодеев в базе" (hitler, stalin, lenin)

-- Ищем по цвету волос ('Black Hair', 'White Hair', 'Red Hair')

-- Попробуйте сделать запрос похожий, но hair in этот кортеж
SELECT * FROM MarvelCharacters 
WHERE 
    hair  IN ('Black Hair', 'White Hair', 'Red Hair')
    AND APPEARANCES > 10
ORDER BY hair, APPEARANCES DESC;

-- LIMIT
-- OFFSET
SELECT * FROM MarvelCharacters 
ORDER BY APPEARANCES DESC
LIMIT 10
OFFSET 10;



-- LIKE- похоже на или КАК
-- % - любое количество символов
-- _ - один символ

SELECT name, APPEARANCES, year
FROM MarvelCharacters
WHERE name LIKE '%Spider%'