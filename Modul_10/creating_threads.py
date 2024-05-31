import time

from threading import Thread


numerics = [x for x in range(1, 11)]
alphabet = [chr(i) for i in range(97, 107)]


def my_print(lst: list):
    for a in lst:
        print(a)
        time.sleep(1)


thread1 = Thread(target=my_print, args=(numerics,))
thread2 = Thread(target=my_print, args=(alphabet,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()
