# Задача:
#
#     Создайте новый класс Buiding
#     Создайте инициализатор для класса Buiding, который будет задавать целочисленный атрибут
#     этажности self.numberOfFloors и строковый атрибут self.buildingType
#     Создайте(перегрузите) __eq__, используйте атрибут numberOfFloors и buildingType для сравнения

class Buiding():
    def __init__(self, x: int, y: str):
        self.numberOfFloors = x
        self.buildingType = y

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType

    def __str__(self) -> str:
        return f'{self.numberOfFloors}  {self.buildingType}'


d = Buiding(1, 'ggg')
d1 = Buiding(2, 'ppp')
d2 = Buiding(2, 'ppp')
print(d == d1)
print(d1 == d2)
print(d2 == d)
