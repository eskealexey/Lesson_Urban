class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print("{} снесен, но он останется в истории".format(self.name))

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return 'Название: {}, кол-в этажей: {}'.format(self.name, self.number_of_floors)

    def __eq__(self, other):
        if isinstance(other, House):
            if self.number_of_floors == other.number_of_floors:
                return True
            else:
                return False

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
            return self

    def __iadd__(self, other):
        if isinstance(other, int):
            self.number_of_floors += other
            return self

    def __radd__(self, other):
        if isinstance(other, int):
            self.number_of_floors += other
            return self

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def go_to(self, new_floor: int):
        if new_floor > self.number_of_floors or new_floor <= 0:
            print('Такого этажа не существует')
        else:
            for floor in range(1, new_floor + 1):
                print(floor)


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрешки', 20)
print(House.houses_history)

del h2
del h3
print(House.houses_history)
