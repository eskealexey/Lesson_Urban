from random import choice


# Лямбда-функции
first = 'Мама мыла раму'
second = 'Рамена мало было'

lst_ = list(map(lambda a, b: a == b, first, second))
print(lst_)


# Замыкание
def get_advanced_writer(file_name: str):
    def write_everything(*data_set):
        with open(file=file_name, mode="w", encoding="utf8") as f:
            for val in data_set:
                f.write(str(val) + '\n')
    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


# Метод __call__:
class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное', 'Может быть', 'Никогда')
print(first_ball())
print(first_ball())
print(first_ball())
