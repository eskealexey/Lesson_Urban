#     Создайте новый проект в PyCharm
#     Запустите созданный проект
#
# Ваша задача:
#
#     Создайте новую функцию def test_function
#     Создайте другую функцию внутри функции inner_function, функция должна печатать значение "Я в области видимости функции test_function"
#     Вызовите функцию inner_function внутри функции test_function
#     Попробуйте вызывать inner_function вне функции test_function и посмотрите на результат выполнения программы
#     Полученный код напишите в ответ к домашему заданию
def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()

# inner_function()    # при вызове функции ошибка: NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?
                    # так как функция находится в области видимости функции test_function()

test_function()