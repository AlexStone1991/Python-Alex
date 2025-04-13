-- # TODO Тема SQL. Ч1. Установка софта. Первые SELECT. Урок 35.

SELECT *
FROM MarvelCharacters;

-- SQL - декларативная язык, мы описываем то что хотим получить, а не как это сделать.

-- SEELECT - команда для получения данных из базы данных
-- FROM - из какой таблицы
-- WHERE - фильтруем данные по определенному условию
-- ORDER BY - сортируем данные по определенному полю
-- LIMIT - ограничиваем количество выводимых данных
-- OFFSET - пропускаем определенное количество строк
-- DISTINCT - выбираем только уникальные значения

SELECT name, EYE, HAIR, SEX, APPEARANCES
FROM MarvelCharacters
WHERE APPEARANCES > 1000
ORDER BY APPEARANCES DESC;

-- WHERE - доступны булевы вырожения как в Python
-- > < >= <= = !=
-- AND OR NOT
-- BETWEEN - между двумя значениями
-- IN в списке значений
-- LIKE - поиск по шаблону
-- IS NULL - проверка на NULL\

-- Только '' одинарные кавычки
-- название столбцов, псевдонимы, названия таблиц можно в двойных кавычках
-- регистрозависимость для поиска, но не для называния столбцов и таблиц


SELECT name, APPEARANCES
FROM MarvelCharacters
WHERE HAIR = 'Bald' AND APPEARANCES > 10
ORDER BY APPEARANCES DESC;

SELECT DISTINCT HAIR
FROM MarvelCharacters;
-- DISTINCT - выбирает только уникальные значения
SELECT DISTINCT EYE
FROM MarvelCharacters;

SELECT DISTINCT EYE, HAIR
FROM MarvelCharacters
WHERE EYE IS NOT NULL AND HAIR IS NOT NULL;

SELECT DISTINCT SEX
FROM MarvelCharacters;

SELECT name, SEX
FROM MarvelCharacters
WHERE SEX = 'Agender Characters';

SELECT *
FROM MarvelCharacters
WHERE year IS NOT NULL
ORDER BY year;

SELECT *
FROM MarvelCharacters
WHERE 
    year IS NOT NULL
    AND year > 1939
    AND year < 1946;
-- Вариант 2. BEETWEEN мы можем указать диапазон значений
SELECT * FROM MarvelCharacters
WHERE
    year IS NOT NULL
    AND year BETWEEN 1939 AND 1945;

-- Третий вариант IN вхождение в список значений
SELECT * fROM MarvelCharacters
WHERE
    year IS NOT NULL
    AND year IN (1939, 1940, 1941, 1942, 1943, 1944, 1945);

-- Ищем "злодеев в базе" (hitler, stalin, lenin)
-- Ищем по цвету волос ('Black Hair', 'White Hair', 'Red Hair')
-- попробуйте сделать запрос похожий, но HAIR in этот кортеж
SELECT * FROM MarvelCharacters
WHERE 
    HAIR IN ('Black Hair', 'White Hair', 'Red Hair')
    AND APPEARANCES > 10
ORDER BY hair, APPEARANCES DESC;

SELECT * FROM MarvelCharacters
ORDER BY APPEARANCES DESC
LIMIT 10
OFFSET 10;

-- LIKE - похоже на или КАК
-- % - любое колличество символов
-- _ - один символ

SELECT name, APPEARANCES, year
FROM MarvelCharacters 
WHERE name LIKE '%Spider%man%';