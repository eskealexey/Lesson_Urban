class Vehicle:
    _COLOR_VARIANS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        print("Модель: {}".format(self.__model))

    def get_horsepower(self):
        print('Мощность двигателя: {}'.format(self.__engine_power))

    def get_color(self):
        print('Цвет: {}'.format(self.__color))

    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print('Владелец: {}'.format(self.owner))

    def set_color(self, color):
        if color.lower() in self._COLOR_VARIANS:
            self.__color = color
        else:
            print('Нельзя сменить цвет на {}'.format(color))


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def get_passenger(self):
        print('Количество пассажиров: {}'.format(self.__PASSENGERS_LIMIT))


v1 = Sedan('Fedos', 'Toyta', 'blue', 250)
v1.print_info()
v1.set_color('Pink')
v1.set_color('BLACK')
v1.owner = 'Vasyok'

v1.print_info()
v1.get_passenger()