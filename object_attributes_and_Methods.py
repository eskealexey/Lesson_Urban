# Задача:
#
#     Создайте новый класс House
#     Задайте ему новый атрибут numberOfFloors = 10
#     В цикле пройдитесь по атрибуту numberOfFloors и распечайте значение "Текущий этаж равен"
#     Полученный код напишите в ответ к домашему заданию
#     Что-то я не совсем понял в задании про цикл :(
class House():
    """
    Описание класса House
    """
    def __init__(self,numberOfFloors=10):
        self.numberOfFloors = numberOfFloors

    def view_floor(self):
        print(f'Текущий этаж равен {self.numberOfFloors}')


home = House()
home.view_floor()
home.numberOfFloors = 5
home.view_floor()