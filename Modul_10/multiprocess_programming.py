from multiprocessing import Process, Lock, Manager


class WarehouseManager:
    def __init__(self, shared_data, lock):
        self.lock = lock
        self.data = shared_data

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
        processes = []
        for request in requests:
            p = Process(target=self.process_request, args=(request,))
            processes.append(p)
            p.start()
        for p in processes:
            p.join()


if __name__ == "__main__":
    requests = [
        ("product1", "receipt", 100),
        ("product2", "receipt", 150),
        ("product1", "shipment", 30),
        ("product3", "receipt", 200),
        ("product2", "shipment", 50)
    ]
    with Manager() as manager:
        shared_data = manager.dict()
        lock = Lock()
        warehouse_manager = WarehouseManager(shared_data, lock)
        warehouse_manager.run(requests)

        print(shared_data)
