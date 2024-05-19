# Задание:
#     Создайте минимум два своих собственных исключения, наследуя их от класса Exception. Например, InvalidDataException
#     и ProcessingException.
#     Напишите функцию, которая генерирует различные исключения в зависимости от передаваемых ей аргументов.
#     Добавьте обработку исключений в функции, вызывающие вашу функцию, и передайте исключения дальше по стеку вызовов.
#     В основной части программы вызовите эти функции и корректно обработайте

class InvalidDataException(Exception):
    pass


class ProcessingException(Exception):
    pass


def dividing_numbers(a: int, b: int) -> float:
    if b == 0:
        raise InvalidDataException('Делитель не может быть равен нулю')
    return a / b


def only_digital(stroka: str):
    if not stroka.isdigit():
        raise ProcessingException('В строке есть не цифры')
    return stroka


try:
    print(dividing_numbers(12, 6))
except InvalidDataException as err:
    print(f'{err}')
str_ = input("Введите данные - ")
try:
    print(only_digital(str_))
except ProcessingException as exc:
    print(f'{exc}')
