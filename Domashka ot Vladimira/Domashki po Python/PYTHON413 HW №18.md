---
project: "[[Академия TOP]]"
journal: "[[PYTHON413]]"
tags:
  - PYTHON413
date: 2024-12-14
type:
  - home work
hw_num: 18
topic: Генератор пословиц на Python
hw_theme:
  - python
  - print, f-string
  - random
  - set
  - list
  - while
  - input
st_group: python 413
links:
---

# Домашнее задание 📃
**Генератор пословиц на основе случайных замен.**

Я попросил ChatGPT написать 50 пословиц про ум. Это уже само по себе кладезь мудрости. 😅

Однако мы сделаем генератор пословиц на основе этих данных 🧠

Так же он сгенерировал существительные мужского рода, для генерации `мудрости` 🙂

## Набор данных для работы 💽
```python
proverbs = [
    "Ум хорошо, а два лучше.",
    "Ум — горячая штука.",
    "Ум всё голова.",
    "Умом Россию не понять.",
    "Ум бережет, а глупость губит.",
    "Ум в голову приходит.",
    "Ум от ума не горит.",
    "Умом нагружен, а волосы развеваются.",
    "Умом обдумал, а ногами пошел.",
    "Ум — сокровище, не пропадет без него и копье на ветру.",
    "Ум — грех, а бес — мера.",
    "Ум есть богатство.",
    "Ум роднит народы.",
    "Ум краток, да забот — бездна.",
    "Ум не камень, взял и положил.",
    "Ум не велит, а наставляет.",
    "Ум с мерой, а глупость без меры.",
    "Ум — сокол, глаз его — телескоп.",
    "Ум — не конская морда, не разобьешь.",
    "Ум — семь пядей во лбу.",
    "Ум — не барсук, в нору не залезет.",
    "Ум в голове, а не на ветру.",
    "Ум греет душу, а глупость терпение.",
    "Ум служит человеку, а глупость — хозяином.",
    "Ум мил, да безумству хозяин.",
    "Ум в труде, да наслаждение в праздности.",
    "Ум глаза исправляет.",
    "Ум человека не обманешь.",
    "Ум на подобии огня — без сна не останешься.",
    "Ум к уму приходит.",
    "Ум с пользой тратит время.",
    "Ум желание творит.",
    "Ум общего дела дело.",
    "Ум — друг, а воля — враг.",
    "Ум — бесценное сокровище.",
    "Ум тонок, да разум невелик.",
    "Ум — враг бедности.",
    "Ум — теремок, да не на прокол.",
    "Ум силен, да не камень.",
    "Ум рассудит, что сердце не посоветует.",
    "Ум — подкова, а топор — ось.",
    "Ум легче камня, да весомей золота.",
    "Ум не вешать на гроздья.",
    "Ум — не мешок, на плечи не вешай.",
    "Ум — лучшая победа.",
    "Ум — в суде велик, а в деле своем мал.",
    "Ум голове краса.",
    "Ум — сокровище, а глупость — нищета.",
    "Ум человека — огонь, а глаза — масло.",
    "Ум — путь, а дорога — конец.",
    "Ум стоит денег.",
    "Ум от смеха бьет в ладоши.",
    "Ум — коза, к барскому плечу привыкает.",
    "Ум — лезвие, а лень — ржавчина.",
    "Ум на вершине — мир в руках.",
]

variants = [
    'кот',
    'шеф',
    'мозг',
    'лес',
    'фолк',
    'код',
    'рот',
    'мёд',
    'лук',
    'лес',
    'год',
    'час',
    'друг',
    'муж',
    'айфон',
    'стол',
    'нос',
    'сыр',
    'хлеб',
    'мир',
    'свет',
    'рок',
    'дед',
    'дом',
    'сон',
    'глаз',
    'торт', 
    'драйв', 
    'байк', 
    'джаз', 
    'грим', 
    'рэп', 
    'старт', 
    'пинг-понг', 
    'каприз', 
    'драйф', 
    'размах', 
    'панк', 
    'размер', 
    'перекус', 
    'блеск', 
    'накал', 
    'размен', 
    'кураж', 
    'форсаж', 
    'прорыв'
]
```



### Технологии: 🦾
- Python
- Библиотека `random` (опционально)

## Задание 👷‍♂️

### Описание задачи

1. **Запрос на количество пословиц:**
   - В начале программы запросите у пользователя, сколько пословиц он хочет получить.

2. **Инициализация списков:**
   - Объявите переменные:
     - Пустой список для хранения результатов.
     - Два предоставленных списка: `proverbs` (список пословиц) и `variants` (список существительных).

3. **Цикл для генерации пословиц:**
   - В цикле выполняйте следующие шаги:
     1. Выбирайте случайный элемент из списка пословиц и удаляйте его из списка.
     2. Выбирайте случайное существительное из списка вариантов и также удаляйте его.
     3. Заменяйте слово "ум" в выбранной пословице на выбранное существительное.
     4. Добавляйте измененную пословицу в список результатов.

4. **Завершение цикла:**
   - Цикл продолжается до тех пор, пока не будет создано необходимое количество пословиц, запрошенное пользователем или вы не достигнете лимита.

### Таблица классов и функций:

| Название переменной/функции | Описание                                      | Тип                           |
| --------------------------- | --------------------------------------------- | ----------------------------- |
| `proverbs`                  | Список исходных пословиц                      | `list[str]`                   |
| `variants`                  | Список существительных для замены             | `list[str]`                   |
| `results`                   | Список сгенерированных пословиц               | `list[str]`                   |
| `random.choice`             | Функция для случайного выбора элемента        | `function` из модуля `random` |
| `random.shuffle`            | Функция для случайного перемешивания списка   | `function` из модуля `random` |
| `random.randint`            | Функция для получения случайного целого числа | `function` из модуля `random` |
| `set(proverbs)`             | Преобразование списка пословиц в множество    | `set`                         |
### Варианты работы с рандомом

| Функция          | Описание                                                |
|------------------|---------------------------------------------------------|
| `random.choice`  | Выбирает случайный элемент из списка                    |
| `random.shuffle` | Перемешивает элементы списка                            |
| `random.randint` | Генерирует случайное целое число в указанном диапазоне  |
| `set(proverbs)`  | Преобразует список в множество для уникальных значений  |

## Критерии проверки 👌

>[!warning]
>
>1. Код работает и выполняет задачу по замене слов в пословицах.
>2. Используется цикл `while` или `for` для генерации пословиц.
>3. Результат представлен в виде списка.
>4. Пословицы не повторяются.
>5. Соответствие стандартам `PEP-8`.
>6. Это творческое задание, вы можете выполнить его РАЗНЫМИ способами (как в плане работы с коллекциями так и в плане генерации новых пословиц)

---