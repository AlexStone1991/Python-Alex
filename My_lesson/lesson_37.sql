-- TODO SQL. Ч3. Нормальные формы. Join Выборки. Урок 37

SELECT name, eye_id
FROM MarvelCharacters;

SELECT name, color
FROM MarvelCharacters
JOIN EyeColor ON MarvelCharacters.eye_id = EyeColor.eye_id;

SELECT MarvelCharacters.name, EyeColor.color
FROM MarvelCharacters
JOIN EyeColor ON MarvelCharacters.eye_id = EyeColor.eye_id;

SELECT mc.name, ec.color
FROM MarvelCharacters AS mc
JOIN EyeColor AS ec ON mc.eye_id = ec.eye_id;

SELECT mc.name AS character_name, ec.color AS eye_color
FROM MarvelCharacters AS mc
JOIN EyeColor AS ec ON mc.eye_id = ec.eye_id;


SELECT mc.id AS character_id, mc.name AS character_name, mc.eye_id AS mc_eye_id,
ec.eye_id AS eye_id, ec.color AS eye_color
FROM MarvelCharacters AS mc
JOIN EyeColor AS ec ON mc.eye_id = ec.eye_id;

-- Сделайте запрос JOIN Для получения персонажей с их цветом волос и цветом глаз
-- Вам надо сделать 2 JOIN и явно указать названия таблиц и столбцов

SELECT mc.name AS character_name, ec.color AS eye_color, hc.color AS hair_color
FROM MarvelCharacters AS mc
JOIN EyeColor AS ec ON mc.eye_id = ec.eye_id
JOIN HairColor AS hc ON mc.hair_id = hc.hair_id;


SELECT mc.name AS character_name, ec.color AS eye_color, hc.color AS hair_color
FROM MarvelCharacters AS mc
JOIN EyeColor AS ec ON mc.eye_id = ec.eye_id
JOIN HairColor AS hc ON mc.hair_id = hc.hair_id
WHERE ec.color IN ('Blue Eyes', 'Green Eyes');


SELECT hc.color AS hair_color, COUNT(*) AS num_characters
FROM MarvelCharacters AS mc
JOIN HairColor AS hc ON mc.hair_id = hc.hair_id
GROUP BY hair_color
ORDER BY num_characters DESC;


SELECT hc.color AS hair_color, ec.color AS eye_color, COUNT(*) AS num_characters
FROM MarvelCharacters AS mc
JOIN HairColor AS hc ON mc.hair_id = hc.hair_id
JOIN EyeColor AS ec ON mc.eye_id = ec.eye_id
WHERE mc.APPEARANCES > 50
GROUP BY hc.color, ec.color
HAVING num_characters > 10
ORDER BY num_characters DESC;


-- Напишите запрос выше
-- На основе него напишите запрос с JOIN пол + JOIN Identity и сделайте агрегатную функцию COUNT
-- В выборку WHERE возьмите appearances > 10 + HAVING count > 1
-- Сортировка по count DESC

SELECT s.name AS char_name, i.identity AS char_identity, COUNT(*) AS num_characters
FROM MarvelCharacters AS mc
JOIN sex AS s ON mc.sex_id = s.sex_id
JOIN Identity AS i ON mc.identity_id = i.identity_id
WHERE mc.APPEARANCES > 10
GROUP BY char_name, char_identity
HAVING num_characters > 1
ORDER BY num_characters DESC;

-- Добавим сюда еще их Aligment
SELECT s.name AS sex_name, i.identity AS char_identity, a.name AS char_aligment,
COUNT(*) AS num_characters
FROM MarvelCharacters AS mc
JOIN sex AS s ON mc.sex_id = s.sex_id
JOIN Identity AS i ON mc.identity_id = i.identity_id
JOIN Alignment AS a ON mc.align_id = a.align_id
WHERE mc.APPEARANCES > 10
GROUP BY sex_name, char_identity, char_aligment
HAVING num_characters > 1
ORDER BY sex_name DESC;