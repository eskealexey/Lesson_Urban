from threading import Thread
import time
class Knight(Thread):
    def __init__(self, name, scil, *args, **kwargs):
        super(Knight, self).__init__(*args, **kwargs)
        self.name = name
        self.scil = scil


    def run(self):
        '''Sir Lancelot, сражается 1 день(дня)..., осталось 90 воинов.'''
        day = 0
        enemy = 100
        print(f'{self.name}, на нас напали!')
        while enemy > 0:
            enemy = enemy - self.scil
            time.sleep(1)
            day += 1
            print(f'{self.name}, сражается {day} день(дня)..., осталось {enemy} воинов.')
        print(f'{self.name}, одержал победу спустя {day} дней(дня).')


knight1 = Knight("Sir Lancelot", 10) # Низкий уровень умения
knight2 = Knight("Sir Galahad", 20) # Высокий уровень умения
knight1.start()
knight2.start()
knight1.join()
knight2.join()
print("Все битвы закончились")


