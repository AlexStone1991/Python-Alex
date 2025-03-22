# TODO ООП. Ч7. Магические методы. Математика. Сравнение. Знакомство с Dataclasses. Урок 28.

# __init__
# __str__
# __repr__
# __bool__
# __len__
# __del__

# Математика

# __add__(self, other) Additional/сложение
# __sub__(self, other) Subtruction/вычетание
# __mul__(self, other) Multiplacation/умножение
# __truediv__(self, other) True Division/деление
# __floordiv__(self, other) Floor Division/ целочисленное
# __mod__(self, other) Modulo/остаток от деления
# __pow__(self, other) Power/Возведение в степень

# __iadd__(self, other)
# __isub__(self, other)
# __imul__(self, other)
# __itruediv__(self, other)
# __ifloordiv__(self, other)
# __imod__(self, other)
# __ipow__(self, other)

# __eq__(self, other)
# __ne__(self, other)
# __lt__(self, other)
# __gt__(self, other)
# __le__(self, other)
# __ge__(self, other)

# class Counter:
#     def __init__(self, value):
#         self.value = value
#     def __add__(self, other):
#         return Counter(self.value + other.value)
    
# counter1 = Counter(5)
# counter2 = Counter(16)
# counter3 = counter1 + counter2
# print(counter3.value) # 21

# class Counter1:
#     def __init__(self, value):
#         self.value = value
#     def __add__(self, other):
#         return Counter(self.value + other)
    
# counter4 = Counter1(30)
# counter5 = counter4 + 5
# print(counter5.value)
# class Counter2:
#     def __init__(self, value):
#         self.value = value
#     def __add__(self, other):
#         return self.value + other
    
# counter6 = Counter2(8)
# result = counter6 + 7
# print(result)

# class Bool1:
#     def __init__(self, value):
#         self.value = value
#     def __bool__(self):
#         return self.value > 0
# def test(bool1):
#     if bool1:
#         print("True")
#     else:
#         print("False")
# bool1 = Bool1(-1)
# test(bool1)
# bool2 = Bool1(6)
# test(bool2)

# class Num:
#     def __init__(self, value):
#         self.value = value
#     def __gt__(self, other):
#         return self.value > other.value
#     def __lt__(self, other):
#         return self.value < other.value
    
# num1 = Num(3)
# num2 = Num(6)

# if num1 > num2:
#     print(f"{num1} больше {num2}")
# elif num1 < num2:
#     print(f"{num1} меньше {num2}")
# else:
#     print("num1 равно num2")

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def __getitem__(self, item):
#         if item == "name":
#             return self.name
#         elif item == "age":
#             return self.age
#         return None
    
# person = Person("Иван", 20)
# print("Name:", person['name'])
# print("Age", person['age'])
# print("Nick:", person['nick'])

# class Person1:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#     def __contains__(self, item):
#         if item == "name" or item == "age":
#             return True
#         return False
    
# ivan1 = Person1("Ivan", 20)

# print("name" in ivan1)
# print("age" in ivan1)
# print("nick" in ivan1)


# задача 1. Необходимо создать класс Airplane
# Используя магические методы реализации
# проверку на равенство типов самолетов (==)
# увеличение и уменьение кол-во пассажиров в салоне


# class Airplane:
#     def __init__(self, model, max_passengers):
#         self.model = model
#         self.max_passengers = max_passengers
#         self.current_passengers = 0
#     def __eq__(self, other):
#         return self.__class__== other.__class__
    
#     def __add__(self, value):
#         self.current_passengers += value
#         if self.current_passengers > self.max_passengers:
#             print(f"Привышено максмальное кол-во {self.current_passengers}")
#         return self
#     def __sub__(self, value):
#         self.current_passengers -= value
#         if self.current_passengers < 0:
#             print(f"Кол-во пассажиров не может быть отрицательным {self.current_passengers}")
#         return self
#     def __iadd__(self, value):
#         return self.__add__(value)
#     def __isub__(self, value):
#         return self.__sub__(value)
#     def __gt__(self, other):
#         return self.max_passengers > other.max_passengers
#     def __lt__(self, other):
#         return self.max_passengers < other.max_passengers
#     def __ge__(self, other):
#         return self.max_passengers >= other.max_passengers
#     def __le__(self, other):
#         return self.max_passengers <= other.max_passengers
    
# airplane1 = Airplane("Boeing 777", 300)

# airplane2 = Airplane("Airbus A320", 200)

# print(airplane1 == airplane2) # False
# print(airplane1.max_passengers)

# airplane1 += 50

# print(airplane1.current_passengers) # 50

# airplane2 -= 70
# print(airplane2.current_passengers)
# print(airplane1 < airplane2)
# print(airplane1 > airplane2)

# class Flat:
#     def __init__(self, area, price):
#         self.area = area
#         self.price = price
#     def __eq__(self, other):
#         return self.area == other.area
    
#     def __ne__(self, other):
#         return self.area != other.area
    
#     def __gt__(self, other):
#         return self.area > other.area
#     def __lt__(self, other):
#         return self.area < other.area
    
# flat1 = Flat(60, 150000)
# flat2 = Flat(45, 110000)
# flat3 = Flat(60, 350000)
# print(flat1 == flat3)
# print(flat1 == flat2)
# print(flat1 < flat3)
# print(flat3 > flat2)
from pprint import pprint

class GameScoreMathError(Exception):
    pass

class GameScore:
    MIN_SCORE = 0
    MAX_SCORE = 1000

    def __init__(self, score):
        self.score = self.validate_score_limit(score)

    def __str__(self):
        return f"Текущий счет: {self.score}"

    def __repr__(self):
        return f"GameScore(score={self.score})"

    def _validate_other_type(self, other):
        if not isinstance(other, GameScore):
            raise TypeError(f"Нельзя сложить GameScore и {type(other)}")

    def validate_score_limit(self, score):
        return self._validate_other_limit(score)

    def _validate_other_limit(self, score):
        if not self.MIN_SCORE <= score <= self.MAX_SCORE:
            raise GameScoreMathError(f"Счет должен быть в диапазоне от {self.MIN_SCORE} до {self.MAX_SCORE}")
        return score

    def __iadd__(self, other: "GameScore"):
        self._validate_other_type(other)
        new_score = self.score + other.score
        self.score = self._validate_other_limit(new_score)
        return self

    def __isub__(self, other: "GameScore"):
        self._validate_other_type(other)
        new_score = self.score - other.score
        self.score = self._validate_other_limit(new_score)
        return self

    def __add__(self, other: "GameScore"):
        self._validate_other_type(other)
        new_score = self.score + other.score
        return GameScore(self._validate_other_limit(new_score))

    def __sub__(self, other: "GameScore"):
        self._validate_other_type(other)
        new_score = self.score - other.score
        return GameScore(self._validate_other_limit(new_score))

    def __bool__(self):
        return bool(self.score)

class Player:
    def __init__(self, scores: GameScore, nickname: str):
        self.scores = scores
        self.nickname = nickname

    def __str__(self):
        return f'Игрок {self.nickname} -> {self.scores}'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other: "Player"):
        return self.scores == other.scores

    def __gt__(self, other: "Player"):
        return self.scores.score > other.scores.score

    def __lt__(self, other: "Player"):
        return self.scores.score < other.scores.score

    def __iadd__(self, other: "GameScore"):
        self.scores += other
        return self

    def __isub__(self, other: "GameScore"):
        self.scores -= other
        return self

    def __add__(self, other: "GameScore"):
        new_scores = self.scores + other
        return Player(scores=new_scores, nickname=self.nickname)

    def __sub__(self, other: "GameScore"):
        new_scores = self.scores - other
        return Player(scores=new_scores, nickname=self.nickname)

    def __bool__(self):
        return bool(self.scores)


p1 = Player(scores=GameScore(200), nickname="Fisher")
p2 = Player(scores=GameScore(190), nickname="Hunter")
p3 = Player(scores=GameScore(320), nickname="Flugger")
p4 = Player(scores=GameScore(530), nickname="Robert")

pprint(p1 == p2)
pprint(p1 > p2)
pprint(p1 < p2)
pprint(p1.scores.score > p2.scores.score)
players = [p1, p2, p3, p4]
players.sort(reverse=True)
pprint(players)
print(players[:3])
players.sort(key=lambda player: player.nickname)
pprint(players)

gs = GameScore(500)

p2 += gs
players.sort(reverse=True)

pprint(players[:3])

active_players = [player for player in players if player]
pprint(active_players)
