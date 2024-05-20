# Задача 1: Фабрика Функций
# Написать функцию, которая возвращает различные математические функции (например, деление, умножение)
# в зависимости от переданных аргументов.
def create_func(par):
    if par == 'mul':
        def multiplication(a,b):
            return a * b
        return multiplication
    elif par == 'div':
        def division(a,b):
            if b == 0:
                raise ZeroDivisionError(f'Делить на ноль нельзя')
            else:
                return a / b
        return division
    else:
        raise Exception('Неверный параметр')
try:
    my_func_multi = create_func('mul')
    my_func_div = create_func('div')
    # my_func_any = create_func('any')
    print(my_func_multi(6, 5))
    print(my_func_div(6,3))
    print(my_func_div(6, 0))
except (Exception, ZeroDivisionError) as err:
    print(err)


# Задача 2: Лямбда-Функции
# Использовать лямбда-функцию для реализации простой операции и написать такую же функцию с использованием def.
# Например, возведение числа в квадрат
quard_ = lambda x: x ** 2
print(quard_(9))
def my_quard(x):
    return x ** 2

print(my_quard(9))


# Задача 3: Вызываемые Объекты
# Создать класс с Rect c полями a, b которые задаются в __init__ и методом __call__,
# который возвращает площадь прямоугольника, то есть a*b.

class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self, *args, **kwargs):
        return self.a * self.b

rect_ = Rect(6, 8)
print(rect_())