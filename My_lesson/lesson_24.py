# TODO ООП Ч3. Инкапсуляция. Приватные методы и атрибуты. Урок 24

# _ это protected - доступно при наследовании
# __ это private - доаступно только внутри класса

class Car:
    def __init__(self, model: str, color: str):
        self.model = model
        self.color = color
        self.__speed = 0 # protected
        self.__max_speed = 200 # private

    def __str__(self):
        return f"Марка: {self.model}, Максимальная скорость: {self.__max_speed}"

    def __validate_speed(self, speed: int):
        """
        Приватный метод-валидатор скорости.
        Проверяет, что скорость не отрицательная и не превышает максимальную.
        """
        if speed < 0:
            raise ValueError("Скорость не может быть отрицательной")
        
        if speed > self.__max_speed:
            raise ValueError("Скорость не может превышать максимальную скорость")
        
    @property
    def speed(self) -> int:
        # Публичный метод для получения скорости
        return self.__speed
        
    @speed.setter
    def speed(self, speed: int):
        """
        Публичный метод для установки скорости.
        Вызывает приватный метод-валидатор.
        """
        self.__validate_speed(speed)
        self.__speed = speed
    @speed.deleter
    def speed(self):
        self.__speed = 0

# class Driver:
#     def __init__(self, name: str, car: Car):
#         self.name = name
#         self.car = car

#     def drive(self, speed: int):
#         print(f"{self.name} сел в {self.car.model}")
#         self.car.set_speed(speed)
#         print(f"{self.name} едет со скоростью {self.car._speed}")

audi = Car("Audi", "red")
print(audi)
audi.speed = 100
print(audi.speed)
audi.speed = 200
print(audi.speed)
del audi.speed
print(audi.speed)

# volga = Car("Volga", "Black")
# driver = Driver("Иосиф", volga)
# driver.drive(100)
# driver.drive(200)
# driver.drive(300)
# print(volga.model)
# print(volga.color)
# print(volga._speed)
# # print(volga.__max_speed)
# print(volga._Car__max_speed)

#  шаблон искажения имени _<ClassName>__<attributeName>

