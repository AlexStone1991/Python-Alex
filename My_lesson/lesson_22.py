# TODO ООП. Ч1. Атрибуты и методы. Класс и экземпляр. Практика. Урок 22.

#  - class
# - нейминг классов UpperCamelCase
# - __init__ - иницилизатор
#  - self - ссылка на экземпляр класса
# - __new__ - как скрытая часть конструктора
# - методы работающие с self - методы экземпляра
# - документация класса и методов

# класс обЪявления
class AdPost:
    promote_rate: float = 0.1
    def __init__(self, title: str, text: str, price: int):
        self.title = title
        self.text = text
        self.price = price
        # self.promote_rate: float = 0.5
    
    def __str__(self) -> str:
        return f"Заголовок: {self.title}, Текст: {self.text[:20]}, цена: {self.price}"
    
    def calculate_promote_cost(self, day: int) -> int:
        promote_cost = int(self.price * (self.promote_rate / 100) * day)
        return promote_cost



ap1 = AdPost("Sony playstation 5. Муха не сидела!", "Новая, красивая, блестящая...!", 20000)
ap2 = AdPost("Видеокарта RTX 3090", "Как новая", 60000)

AdPost.promote_rate = 1

print(ap1)
print(ap2)
print(ap1.calculate_promote_cost(3),"рублей")
print(ap2.calculate_promote_cost(3),"рублей")

