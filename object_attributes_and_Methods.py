# Задача:
#
#     Создайте новый класс House
#     Задайте ему новый атрибут numberOfFloors = 10
#     В цикле пройдитесь по атрибуту numberOfFloors и распечайте значение "Текущий этаж равен"
#     Полученный код напишите в ответ к домашему заданию

class House():
    """
    Описание класса House
    """
    def __init__(self, numberOfFloors=10):
        self.numberOfFloors = numberOfFloors

    def view_floor(self):
        print(f'Текущий этаж равен {self.numberOfFloors}')


home = House(10)
# print(home.numberOfFloors)
for i in range(1, home.numberOfFloors + 1):
    home.numberOfFloors = i
    home.view_floor()

