# Задача:
#     Создайте родительский(базовый) класс Vehicle, который имеет свойство vehicle_type = "none"
#     Создайте родительский(базовый) класс Car, который имеет свойство price = 1000000 и функцию def horse_powers,
#     которая возвращает количество лошидиных сил для автомобиля
#     Создайте наследника класса Car и Vehicle - класс Nissan и переопределите свойство price и vehicle_type,
#     а также переопределите функцию horse_powers
#     Создайте экзмепляр класса Nissan и распечайте через функцию print vehicle_type, price

class Vehicle:
    vehicle_type = "none"


class Car:
    def __init__(self, price=1000000):
        self.price = price

    def horse_powers(self):
        return '220 л.с.'


class Nissan(Car, Vehicle):
    def __init__(self, price=500000):
        self.price = price
        self.vehicle_type = "Not none"

    def horse_powers(self):
        return '110 л.с.'

nissan = Nissan()
print(nissan.vehicle_type, nissan.price)

