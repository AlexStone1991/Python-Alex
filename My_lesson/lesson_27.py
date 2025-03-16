# TODO ООП. Ч6. Наследование. Миксины. Практика. Урок 27.


class Pizza:
    def __init__(self, **kwargs):
        self.size = kwargs.pop('size', 30)
        super().__init__(**kwargs)

class Pie:
    def __init__(self, **kwargs):
        self.size = kwargs.pop('size', 30)
        super().__init__(**kwargs)

class CheeseBorderMixin:
    def __init__(self, **kwargs):
        self.height = kwargs.pop('height', 10)
        super().__init__(**kwargs)
    def add_cheese_border(self):
        print(f"Сырный борт, высотой {self.height} мм Активирован!")

class ThinkCrustMixin:
    def __init__(self, **kwargs):
        self.thickness = kwargs.pop('thickness', 1)
    def add_thin_crust(self):
        print(f"Тонкое тексто, толщиной {self.thickness} мм Активировано!")
# Пицца с сырным бортом
class CheeseBorderPizza(Pizza, CheeseBorderMixin):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_cheese_border()
# тест
print("Пицца с сырным бортом")
pizza = CheeseBorderPizza(size=40, height=20)
print(pizza.size)
print(pizza.height)
print(pizza.__dict__)
print(CheeseBorderPizza.__mro__)

