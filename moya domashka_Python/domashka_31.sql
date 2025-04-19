-- Домашка №31 по SQL

-- Лысые злодеи 90-х годов
SELECT name, FIRST_APPEARANCE, APPEARANCES
FROM MarvelCharacters
WHERE HAIR = 'Bald' AND ALIGN = 'Bad Characters' AND Year BETWEEN 1990 AND 1999;

-- Герои с тайной идентичностью и необычными глазами
SELECT name, FIRST_APPEARANCE, EYE
FROM MarvelCharacters
WHERE identify = 'Secret Identity' AND EYE NOT IN ('Blue', 'Brown', 'Green') AND FIRST_APPEARANCE IS NOT NULL;

-- Персонажи с изменяющимся цветом волос
SELECT name, HAIR
FROM MarvelCharacters
WHERE HAIR = 'Variable Hair';

-- Женские персонажи с редким цветом глаз
-- Женские персонажи с редким цветом глаз
SELECT name, EYE
FROM MarvelCharacters
WHERE SEX = 'Female Characters' AND (EYE LIKE '%Gold%' OR EYE LIKE '%Amber%');


-- Персонажи без двойной идентичности, сортированные по году появления
SELECT name, FIRST_APPEARANCE
FROM MarvelCharacters
WHERE identify = 'No Dual Identity'
ORDER BY Year DESC;

-- Герои и злодеи с необычными прическами
SELECT name, ALIGN, HAIR
FROM MarvelCharacters
WHERE HAIR NOT IN ('Brown', 'Black', 'Blond', 'Red') AND ALIGN IN ('Good Characters', 'Bad Characters');

-- Персонажи, появившиеся в определённое десятилетие
SELECT name, FIRST_APPEARANCE
FROM MarvelCharacters
WHERE Year BETWEEN 1960 AND 1969;

-- Персонажи с уникальным сочетанием цвета глаз и волос
SELECT name, EYE, HAIR
FROM MarvelCharacters
WHERE EYE = 'Yellow Eyes' AND HAIR = 'Red Hair';

-- Персонажи с ограниченным количеством появлений
SELECT name, APPEARANCES
FROM MarvelCharacters
WHERE APPEARANCES < 10;

-- Персонажи с наибольшим количеством появлений
SELECT name, APPEARANCES
FROM MarvelCharacters
ORDER BY APPEARANCES DESC
LIMIT 5;
