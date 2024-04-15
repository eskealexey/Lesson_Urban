# Функция с параметрами по умолчанию:
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print_params()
print_params(10, 5, 'False')
print_params('A', *[1, 2])
print_params(b = 25)
print_params(c = [1,2,3])
print_params(*[10, 20])
print('-' * 30)


# Распаковка параметров:
#
# Создайте список values_list с тремя элементами разных типов.
# Создайте словарь values_dict с тремя ключами, соответствующими параметрам функции print_params, и значениями разных типов.
# Передайте values_list и values_dict в функцию print_params, используя распаковку параметров (* для списка и ** для словаря).

values_list = ['Str_', 100, True]
values_dict = {
    'a': 10,
    'b': False,
    'c': 'Stroka'
}
print_params(*values_list)
print_params(**values_dict)
print('-' * 30)


# Распаковка + отдельные параметры:
# Создайте список values_list_2 с двумя элементами разных типов
# Проверьте, работает ли print_params(*values_list_2, 42)
values_list_2 = ['line', 5.6]
print_params(*values_list_2, 42)