import time
from threading import Condition, Thread

con = Condition()
num = 0


class Producer(Thread):

    def __init__(self):
        super(Producer, self).__init__()

    def run(self):
        global num
        with con:
            while num < 5:
                num += 1
                print('now have {}, continue...'.format(num))
                time.sleep(1)
            con.notify()


class Consumer(Thread):

    def __init__(self):
        super(Consumer, self).__init__()

    def run(self):
        global num
        with con:
            while num > 0:
                num -= 1
                print('have {}, now will consume another'.format(num))
                time.sleep(1)
            con.notify()


if __name__ == '__main__':
    p = Producer()
    c = Consumer()
    p.start()
    c.start()
