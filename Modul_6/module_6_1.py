class Animal:
    alive = True
    fed = False

    def eat(self, food):
        if food.edible:
            print('{} съел {}'.format(self.name, food.name))
            self.fed = True
        else:
            print('{} не стал есть {}'.format(self.name, food.name))
            self.alive = False


class Plant:
    edible = False


class Mammal(Animal):
    def __init__(self, name):
        self.name = name


class Predator(Animal):
    def __init__(self, name):
        self.name = name


class Flower(Plant):
    edible = False

    def __init__(self, name):
        self.name = name


class Fruit(Plant):
    edible = True

    def __init__(self, name):
        self.name = name


a1 = Predator('Волк с Уолт-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик-семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
