# Задача:
#
#     Создайте родительский(базовый) класс Car, который имеет свойство price = 1000000 и функцию def horse_powers,
#     которая возвращает количество лошидиных сил для автомобиля
#     Создайте наследника класса Car - класс Nissan и переопределите свойство price,
#     а также переопределите функцию horse_powers
#     Дополнительно создайте класс Kia, который также будет наследником класса Car и переопределите также свойство price,
#     а также переопределите функцию horse_powers

class Car:
    price = 1000000
    def horse_powers(self):
        print('300 л.с.')

class Nissan(Car):
    price = 500000
    def horse_powers(self):
        print('220 л.с.')

class Kia(Car):
    def __init__(self, price=900000):
        self.price = price

    def horse_powers(self):
        print('170 л.с.')
