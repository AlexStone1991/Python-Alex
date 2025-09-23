# TODO ООП 10. Практика с MistralAI. Урок 32.

# Порождающие паттерны проектирования
# Паттерн Singleton.

# class Singleton:
#     _instance = None

#     def __new__(cls, *args, **kwargs):
#         if not cls._instance:
#             cls._instance = super(Singleton, cls).__new__(cls)
#         return cls._instance
    
#     def __init__(self, value):
#         self.value = value
    
#     def __str__(self):
#         return F"Экземпляр Singleton с значением: {self.value} и индикатором: {id(self)}"
    
# singleton1 = Singleton(10)
# singleton2 = Singleton(20)
# print(singleton1)
# print(singleton2)
# # Экземпляр Singleton с значением: 20 и индикатором: 2244356960144
# # Экземпляр Singleton с значением: 20 и индикатором: 2244356960144

from abc import ABC, abstractmethod
from copy import deepcopy

# class AbcrtactCharacter(ABC):
#     @abstractmethod
#     def clone(self):
#         pass

# class Warrior(AbcrtactCharacter):

#     # класс для создания персонажа-воителя
#     def __init__(self, name: str, health: str, mana: int):
#         self.name = name
#         self.health = health
#         self.damage = mana
    
#     def clone(self):
#         # метод для клонирования персонажа
#         return deepcopy(self)
    
# class Mage(AbcrtactCharacter):
#     # класс для создания персонажа-мага
#     def __init__(self, name: str, health: str, mana: int):
#         self.name = name
#         self.health = health
#         self.damage = mana

#     def clone(self):
#         # метод для клонирования персонажа
#         return deepcopy(self)
    
# class CharRegistrty:
#     # реестр персонажей
#     def __init__(self):
#         self._characters = {}

#     def register_character(self, name: str, character: AbcrtactCharacter):
#         # метод для регистрации персонажа
#         self._characters[name] = character

#     def clone_character(self, name: str) -> AbcrtactCharacter:
#         # метод для клонирования персонажа
#         character = self._characters.get(name)
#         if character is None:
#             raise ValueError(f"Персонаж с именем {name} не найден")
#         return character.clone()
    
#     def get_available_characters(self) -> list[str]:
#         # метод для получения списка доступных персонажей
#         return list(self._characters.keys())
    
# if __name__ == "__main__":
#     # создание персонажей
#     registry = CharRegistrty()

#     # регестрируем персонажей
#     warrior = Warrior("Воин", 100, 20)
#     mage = Mage("Маг", 80, 30)

#     registry.register_character("Воин", warrior)
#     registry.register_character("Маг", mage)

#     # клонируем персонажей
#     cloned_warrior = registry.clone_character("Воин")
#     cloned_mage = registry.clone_character("Маг")

#     # выводим информацию о клонированных персонажах
#     print(f"Клонированный Воин: {cloned_warrior.name}, Здоровье: {cloned_warrior.health}, mana: {cloned_warrior.damage}")
#     print(f"Клонированный Маг: {cloned_mage.name}, Здоровье: {cloned_mage.health}, mana: {cloned_mage.damage}")
from dataclasses import dataclass, field
from typing import Self
# Абстрактный датакласс для продукта
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Self

# Абстрактный датакласс продукта

@dataclass
class AbstractFastfoodProduct(ABC):
    """
    Абстрактный класс продукта быстрого питания.
    """
    name: str
    size: str
    price: float
    meat: str
    sauce: str
    ingredients: list = field(default_factory=list)

    def __str__(self):
        return f"{self.name} ({self.size}) - {self.price} руб. | Мясо: {self.meat}, Соус: {self.sauce}, Ингредиенты: {', '.join(self.ingredients)}"
    
    @abstractmethod
    def om_nom_nom(self):
        """
        Метод для имитации поедания продукта.
        """
        pass


@dataclass
class Shaverma(AbstractFastfoodProduct):
    """
    Класс - продукт строителя для Шавермы.
    """
    name: str
    size: str = field(init=False)
    price: float = field(init=False)
    meat: str = field(init=False)
    sauce: str = field(init=False)
    ingredients: list = field(init=False, default_factory=list)

    def om_nom_nom(self):
        """
        Имитация поедания Шавермы.
        """
        print(f"Упс! Шаверма {self.name} закончилась. Остались только {', '.join(self.ingredients)}.")
        self.ingredients.clear()


@dataclass
class Burger(AbstractFastfoodProduct):
    """
    Класс - продукт строителя для Бургера.
    """
    name: str
    size: str = field(init=False)
    price: float = field(init=False)
    meat: str = field(init=False)
    sauce: str = field(init=False)
    ingredients: list = field(init=False, default_factory=list)

    def om_nom_nom(self):
        """
        Имитация поедания Шавермы.
        """
        print(f"Упс! Бургер {self.name} закончилась. Остались только {', '.join(self.ingredients)}.")
        self.ingredients.clear()


class AbstractFastfoodBuilder(ABC):
    """
    Абстрактный строитель для создания продуктов быстрого питания.
    """
    @abstractmethod
    def reset(self):
        """
        Сбрасывает текущий объект.
        """
        pass

    @abstractmethod
    def set_name(self, name: str):
        pass

    @abstractmethod
    def set_size(self, size: str):
        pass

    @abstractmethod
    def set_price(self, price: float):
        pass

    @abstractmethod
    def set_meat(self, meat: str):
        pass

    @abstractmethod
    def set_sauce(self, sauce: str):
        pass

    @abstractmethod
    def add_ingredient(self, ingredient: str):
        pass

    @abstractmethod
    def get_product(self) -> Self:
        pass


class ShavermaBuilder(AbstractFastfoodBuilder):
    """
    Конкретный строитель для создания Шавермы.
    """
    def __init__(self):
        self.shaverma = self.reset()

    def reset(self):
        """
        Сбрасывает текущий объект Шавермы.
        """
        self.shaverma = Shaverma(name="")
        return self.shaverma
    
    def set_name(self, name: str):
        """
        Устанавливает имя Шавермы.
        """
        self.shaverma.name = name

    def set_size(self, size: str):
        """
        Устанавливает размер Шавермы.
        """
        self.shaverma.size = size

    def set_price(self, price: float):
        """
        Устанавливает цену Шавермы.
        """
        self.shaverma.price = price

    def set_meat(self, meat: str):
        """
        Устанавливает мясо Шавермы.
        """
        self.shaverma.meat = meat

    def set_sauce(self, sauce: str):
        """
        Устанавливает соус Шавермы.
        """
        self.shaverma.sauce = sauce


    def add_ingredient(self, ingredient: str):
        """
        Устанавливает ингредиенты Шавермы.
        """
        self.shaverma.ingredients.append(ingredient)


    def get_product(self) -> Shaverma:
        """
        Возвращает готовую Шаверму.
        """
        return self.shaverma


class Director:
    """
    Директор, который управляет процессом создания продукта.
    """
    def __init__(self, builder: AbstractFastfoodBuilder):
        self.builder = builder

    def construct_shaverma(self, name: str, size: str, price: float, meat: str, sauce: str, ingredients: list):
        """
        Конструирует Шаверму с заданными параметрами.
        """
        self.builder.reset()  # Сбрасываем предыдущий объект
        self.builder.set_name(name)
        self.builder.set_size(size)
        self.builder.set_price(price)
        self.builder.set_meat(meat)
        self.builder.set_sauce(sauce)
        for ingredient in ingredients:
            self.builder.add_ingredient(ingredient)

        return self.builder.get_product()
    

# Тестируем
if __name__ == "__main__":
    # Создаем строителя
    shaverma_builder = ShavermaBuilder()

    # Создаем директора
    director = Director(shaverma_builder)

    # Конструируем Шаверму
    shaverma = director.construct_shaverma(
        name="Шаверма с курицей",
        size="Большая",
        price=150.0,
        meat="Курица",
        sauce="Чесночный",
        ingredients=["Помидоры", "Огурцы", "Лук"]
    )

    print(shaverma)
    # Имитируем поедание Шавермы
    shaverma.om_nom_nom()

    # Создадим Ultra XXL Шаверму c говядиной, пармизаном и соусом BBQ
    shaverma = director.construct_shaverma(
        name="Ultra XXL Шаверма",
        size="Ultra XXL",
        price=300.0,
        meat="Говядина",
        sauce="BBQ",
        ingredients=["Пармизан", "Помидоры", "Огурцы", "Лук"]
    )

    print(shaverma)
    shaverma.om_nom_nom()