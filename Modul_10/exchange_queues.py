import queue
import threading
import time


class Table:

    def __init__(self, number):
        self.number = number
        self.is_busy = False


class Cafe:

    def __init__(self, tables_):
        self.tables = tables_
        self.queue = queue.Queue()

    def customer_arrival(self, number_of_customers=20):
        i = 0
        while True:
            if self.check_table_not_busy() and not self.queue.empty():
                self.serve_customer(self.queue.get())
            if i < number_of_customers:
                i += 1
                self.serve_customer(Customer(i, self.tables))
            time.sleep(1)
            if self.queue.empty() and i >= number_of_customers:
                break

    def serve_customer(self, customer):
        if self.check_table_not_busy():
            customer.start()
        else:
            self.queue.put(customer)
            print(f'Посетитель номер {customer.number} ожидает свободный стол')

    def check_table_not_busy(self):
        if any((not table.is_busy) for table in self.tables):
            return True
        else:
            return False


class Customer(threading.Thread):

    def __init__(self, num, tables_):
        super().__init__()
        print(f'Посетитель номер {num} прибыл')
        self.number = num
        self.tables = tables_

    def run(self):
        for table in self.tables:
            if not table.is_busy:
                table.is_busy = True
                print(f'Посетитель номер {self.number} сел за стол {table.number}')
                time.sleep(5)
                table.is_busy = False
                print(f'Посетитель номер {self.number} покушал и ушел')
                return


tables = [Table(x) for x in range(1, 4)]

cafe = Cafe(tables)

customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

customer_arrival_thread.join()
