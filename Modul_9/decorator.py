# Задание:
# Напишите 2 функции:
#
#     Функция которая складывает 3 числа (sum_three)
#     Функция декоратор (is_prime), которая распечатывает "Простое",
#     если результат 1ой функции будет простым числом и "Составное" в противном случае.

def is_prime(func):
    def wrapper(*args, **kwargs):
        count = 0
        result = func(*args, **kwargs)
        g = (x for x in range(2, result + 1))
        for i in g:
            if result % i == 0:
                count += 1
                if count >= 2:
                    break
        if count >= 2:
            print("Составное")
        else:
            print('Простое')
        return result

    return wrapper


@is_prime
def sum_three(a: int, b: int, c: int) -> int:
    return a + b + c


f = sum_three
print(f(2, 3, 6))
