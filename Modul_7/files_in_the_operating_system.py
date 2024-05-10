#     Используйте os.walk для обхода каталога, путь к которому указывает переменная directory
import os
import datetime

directory = os.getcwd()
path_ = os.walk(directory)
#     Примените os.path.join для формирования полного пути к файлам.
for dirpath, dirname, filename in path_:
    print(dirpath)
    print(dirname)
    print(filename)
#   Примените os.path.join для формирования полного пути к файлам.
    for f in filename:
        full = os.path.join(dirpath, f)
#   Используйте os.path.getmtime и модуль time для получения и отображения времени последнего изменения файла.
        time_f = os.path.getmtime(full)
#   Используйте os.path.getsize для получения размера файла.
        size_f = os.path.getsize(full)
        # print(f'Файл:{full}, время создания:{time_f}(в сек.) =>> формат даты: {datetime.datetime.fromtimestamp(time_f)},'
        #       f' Размер: {size_f} Байт')
        print(
            f'Файл:{full}, время создания: {datetime.datetime.fromtimestamp(time_f)}, Размер: {size_f} Байт')
#   Используйте os.path.dirname для получения родительской директории файла.
        print(f'Родительская директория {os.path.dirname(full)}')