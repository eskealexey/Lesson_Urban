from multiprocessing import Process, Lock


class WarehouseManager:
    def __init__(self, *args, **kwargs):
        self.lock = Lock()
        self.data = {}

    def process_request(self, request: tuple):
        product, action, quantity = request
        with self.lock:
            if action == 'receipt':
                if product in self.data:
                    self.data[product] += quantity
                else:
                    self.data[product] = quantity
            elif action == 'shipment':
                if product in self.data and self.data[product] >= quantity:
                    self.data[product] -= quantity

    def run(self, requests):
        mang_list = []
        for i in requests:
            self.manag = Process(target=self.process_request, args=(i,))
            mang_list.append(self.manag)
            self.manag.start()
        for i in requests:
            self.manag.join()

if __name__ == "__main__":
    manager = WarehouseManager()
    shared_data = manager.dict()  # Создаем общий словарь
    lock = Lock()

    requests = [
        ("product1", "receipt", 100),
        ("product2", "receipt", 150),
        ("product1", "shipment", 30),
        ("product3", "receipt", 200),
        ("product2", "shipment", 50)
    ]

    warehouse_manager = WarehouseManager(shared_data, lock)
    warehouse_manager.run(requests)

    print(shared_data)
