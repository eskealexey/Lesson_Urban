#     Атрибут data - словарь, где ключ - название продукта, а значение - его кол-во. (изначально пустой)
#     Метод process_request - реализует запрос (действие с товаром), принимая request - кортеж.
#
# Есть 2 действия: receipt - получение, shipment - отгрузка.
# а) В случае получения данные должны поступить в data (добавить пару, если её не было и изменить значение ключа,
# если позиция уже была в словаре)
# б) В случае отгрузки данные товара должны уменьшаться (если товар есть в data и если товара больше чем 0).
# 3.Метод run - принимает запросы и создаёт для каждого свой параллельный процесс, запускает его(start)
# и замораживает(join).
from multiprocessing import Process, Lock


class WarehouseManager:
    def __init__(self):
        self.data = {}

    def process_request(self, request: tuple):
        dict_tmp = {request[0]: request[2]}
        if request[1] == 'receipt':
            if request[0] not in self.data:
                self.data.update(dict_tmp)
            elif request[0] in self.data:
                val = self.data[request[0]]
                self.data[request[0]] = val + request[2]
        if request[1] == 'shipment':
            if request[0] not in self.data or self.data[request[0]] <= 0:
                pass
            else:
                val = self.data[request[0]]
                self.data[request[0]] = val - request[2]

    def run(self, request):
        for i in request:
            self.process_request(i)


# Множество запросов на изменение данных о складских запасах
requests = [
    ("product1", "receipt", 100),
    ("product2", "receipt", 150),
    ("product1", "shipment", 30),
    ("product3", "receipt", 200),
    ("product2", "shipment", 50),
    ("product3", "receipt", 200)
]


manager = WarehouseManager()

# Запускаем обработку запросов
manager.run(requests)

# Выводим обновленные данные о складских запасах
print(manager.data)
