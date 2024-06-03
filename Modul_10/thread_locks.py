from threading import Thread, Lock


class BankAccount:
    amount = 1000

    def deposit(self, amount):
        with lock:
            self.amount += amount
            print(f'Добавляем - {amount}, новый баланс - {self.amount}')

    def withdraw(self, amount):
        with lock:
            self.amount -= amount
            print(f'Снимаем - {amount}, новый баланс - {self.amount}')


def deposit_task(ac, amount):
    for _ in range(5):
        ac.deposit(amount)


def withdraw_task(ac, amount):
    for _ in range(5):
        ac.withdraw(amount)


lock = Lock()
account = BankAccount()

deposit_thread = Thread(target=deposit_task, args=(account, 100))
withdraw_thread = Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()
