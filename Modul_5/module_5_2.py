class House():

    def __init__(self, name: str, number_of_floors: int):
        self.name =name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return 'Название: {}, кол-в этажей: {}'.format(self.name, self.number_of_floors)

    def go_to(self, new_floor: int):
        if new_floor > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            for floor in range(1, new_floor + 1):
                print(floor)



h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)


print(h1)
print(h2)
print(len(h1))
print(len(h2))



