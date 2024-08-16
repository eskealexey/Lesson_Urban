def personal_sum(numbers):
    result = 0
    correct = 0
    for a in numbers:
        try:
            result += a
            correct += 1
        except TypeError:
            print('Некорректный тип данных для подсчета суммы - {}'.format(a))
    return result, correct


def calculate_average(numbers):
    try:
        result = personal_sum(numbers)
        return result[0] / result[1]
    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных ')
        return


print('Результат 1: {}'.format(calculate_average('1, 2, 3')))
print('Результат 2: {}'.format(calculate_average([1, 'Строка', 3, 'Еще строка'])))
print('Результат 3: {}'.format(calculate_average(567)))
print('Результат 4: {}'.format(calculate_average([42, 15, 36, 13])))
