# TODO ООП. Ч6. Наследование. Миксины. Практика. Урок 27.

# Пример использования миксинов

class Pizza:
    def __init__(self, size: int):
        self.size = size

class Pie:
    def __init__(self, size: int):
        self.size = size

class CheeseBorderMixin:
    def add_cheese_border(self):
        print("Сырный борт Активирован!")

class ThinkCrustMixin:
    def add_thin_crust(self):
        print("Тонкое тексто Активировано!")

# 1 нам нужна Пицца Делаем экземплят класса Pizza
# pizza = Pizza(30)

# 2 нам нужна мутация - пицца с сырным бортом делаем экземпляр класса PizzaCheeseBorder

class PizzaWithCheeseBorder(Pizza, CheeseBorderMixin):
    def __init__(self, size: int):
        super().__init__(size)
        self.add_cheese_border()

# пирог с сырным бортом и тонким тестом

class PieCheeseBorderThinCrust(Pie, CheeseBorderMixin, ThinkCrustMixin):
    def __init__(self, size: int):
        super().__init__(size)
        

p = PieCheeseBorderThinCrust(30)
print(p.size)
p.add_cheese_border()
p.add_thin_crust()