-- ОСНОВНЫЕ ЗАДАНИЯ
-- 1. Общее количество персонажей по статусу
SELECT ALIVE, COUNT(*)
FROM MarvelCharacters
GROUP BY ALIVE;

-- 2. Среднее количество появлений персонажей с разным цветом глаз
SELECT EYE, AVG(APPEARANCES)
FROM MarvelCharacters
-- WHERE EYE IS NOT NULL
GROUP BY EYE
ORDER BY AVG(APPEARANCES);

-- 3. Максимальное количество появлений у персонажей с определенным цветом волос
SELECT HAIR, MAX(APPEARANCES)
FROM MarvelCharacters
GROUP BY HAIR
ORDER BY MAX(APPEARANCES) DESC;

-- 4. Минимальное количество появлений среди персонажей с известной и публичной личностью
SELECT identify, MIN(APPEARANCES)
FROM MarvelCharacters
WHERE identify LIKE '%public%'
GROUP BY identify
ORDER BY MIN(APPEARANCES);

-- 5. Общее количество персонажей по полу. у Вас скорее всего опечатка в этом задании.
-- Сделал селект по полу
SELECT SEX, COUNT(*)
FROM MarvelCharacters
GROUP BY SEX;

-- 6. Средний год первого появления персонажей с различным типом личности
SELECT identify, AVG(year)
FROM MarvelCharacters
GROUP BY identify
ORDER BY AVG(year);

-- 7. Количество персонажей с разным цветом глаз среди живых
SELECT EYE, COUNT(*)
FROM MarvelCharacters
WHERE ALIVE LIKE '%living%'
-- AND EYE IS NOT NULL
GROUP BY EYE
ORDER BY COUNT(*) DESC;

-- 8. Максимальное и минимальное количество появлений среди персонажей с определенным цветом волос
SELECT HAIR, MAX(APPEARANCES), MIN(APPEARANCES)
FROM MarvelCharacters
GROUP BY HAIR
ORDER BY MAX(APPEARANCES) DESC, MIN(APPEARANCES);

-- 9. Количество персонажей с различным типом личности среди умерших
SELECT identify, COUNT(*)
FROM MarvelCharacters
WHERE ALIVE LIKE '%deceased%'
GROUP BY identify
ORDER BY COUNT(*) DESC;

-- 10. Средний год первого появления персонажей с различным цветом глаз
SELECT EYE, AVG(year)
FROM MarvelCharacters
GROUP BY EYE
ORDER BY AVG(year);

-- ПОДЗАПРОСЫ
-- 11. Персонаж с наибольшим количеством появлений
SELECT name, APPEARANCES
FROM MarvelCharacters
WHERE APPEARANCES = (SELECT MAX(APPEARANCES) FROM MarvelCharacters);

-- 12. Персонажи, впервые появившиеся в том же году, что и персонаж с максимальными появлениями
SELECT name, year
FROM MarvelCharacters
WHERE year = (SELECT year FROM MarvelCharacters WHERE APPEARANCES = (SELECT MAX(APPEARANCES) FROM MarvelCharacters));

-- 13. Персонажи с наименьшим количеством появлений среди живых
SELECT name, APPEARANCES
FROM MarvelCharacters
WHERE APPEARANCES = (SELECT MIN(APPEARANCES) FROM MarvelCharacters WHERE ALIVE LIKE '%living%');

-- 14. Персонажи с определенным цветом волос и максимальными появлениями среди такого цвета
SELECT name, HAIR, APPEARANCES
FROM MarvelCharacters
WHERE HAIR = 'Red Hair' AND APPEARANCES = (SELECT MAX(APPEARANCES) FROM MarvelCharacters WHERE HAIR = 'Red Hair');

-- 15. Персонажи с публичной личностью и наименьшим количеством появлений
SELECT name, identify, APPEARANCES
FROM MarvelCharacters
WHERE identify LIKE '%public%'
    AND APPEARANCES = (SELECT MIN(APPEARANCES) FROM MarvelCharacters WHERE identify LIKE '%public%');