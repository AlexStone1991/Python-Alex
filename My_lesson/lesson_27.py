# TODO ООП. Ч6. Наследование. Миксины. Практика. Урок 27.


class Pizza:
    def __init__(self, size: int):
        self.size = size

class Pie:
    def __init__(self, size: int):
        self.size = size

class CheeseBorderMixin:
    def add_cheese_border(self, height: int = 10):
        self.height = height
        result = f"Сырный борт, высотой {self.height} мм Активирован!"
        print(result)
        return result

class ThinkCrustMixin:
    def add_thin_crust(self, thickness: int = 1):
        self.thickness =thickness
        print(f"Тонкое тексто, толщиной {self.thickness} мм Активировано!")
# Пицца с сырным бортом

class CheeseBorderPizza(Pizza, CheeseBorderMixin):
    def __init__(self, size: int, height: int = 10):
        super().__init__(size)
        self.add_cheese_border(height)
# тест
cbp = CheeseBorderPizza(30)
print(cbp.size)