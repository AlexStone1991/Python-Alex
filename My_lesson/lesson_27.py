# TODO ООП. Ч6. Наследование. Миксины. Практика. Урок 27.

# Пример использования миксинов

class Pizza:
    def __init__(self, size: int):
        self.size = size

class Pie:
    def __init__(self, size: int):
        self.size = size

class CheeseBorderMixin:
    def __init__(self, height: int):
        self.height = height
    def add_cheese_border(self):
        print(f"Сырный борт, высотой {self.height} мм Активирован!")

class ThinkCrustMixin:
    def __init__(self, thickness: int):
        self.thickness = thickness
    def add_thin_crust(self):
        print(f"Тонкое тексто, толщиной {self.thickness} мм Активировано!")

# 1 нам нужна Пицца Делаем экземплят класса Pizza
# pizza = Pizza(30)

# 2 нам нужна мутация - пицца с сырным бортом делаем экземпляр класса PizzaCheeseBorder

class PizzaWithCheeseBorder(Pizza, CheeseBorderMixin):
    def __init__(self, size: int, height: int):
        Pizza.__init__(self, size)
        CheeseBorderMixin.__init__(self, height)
