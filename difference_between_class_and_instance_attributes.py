# Здача:
#     Создайте новый класс Buiding с атрибутом total
#     Создайте инициализатор для класса Buiding, который будет увеличивать атрибут количества
#     созданных объектов класса Building total (по примеру класса Lemming из урока)
#     В цикле создайте 40 объектов класса Building и выведите их на экран командой print

class Buiding():
    total = 0

    def __init__(self):
        Buiding.total += 1
        self.total = Buiding.total

    def __str__(self):
        return (f"Объект класса Buiding № {self.total} ")


hauses = [(f"home{i}") for i in range(1, 41)]

for j in range(len(hauses)):
    hauses[j] = Buiding()
    print(hauses[j])
