# TODO ООП Ч3. Инкапсуляция. Приватные методы и атрибуты. Урок 24

# _ это protected - доступно при наследовании
# __ это private - доаступно только внутри класса

class Car:
    def __init__(self, color: str, model: str):
        self.model = model
        self.color = color
        self._speed = 0 # protected
        self.__max_speed = 200 # private

    def __str__(self):
        return f"Марка: {self.model}, Максимальная скорость: {self.__max_speed}"

volga = Car("Volga", "Black")
print(volga.model)
print(volga.color)
print(volga._speed)
# print(volga.__max_speed)
print(volga._Car__max_speed)

#  шаблон искажения имени _<ClassName>__<attributeName>