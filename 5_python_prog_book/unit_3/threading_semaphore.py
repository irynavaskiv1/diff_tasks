import threading
import time

semaphore = threading.Semaphore(1)
item = []


def producer():
    global item
    print('producer() working!')
    with semaphore:
        item.append('item')
        x = 5
        while x >= 0:
            print('x: ', x)
            x -= 1
            time.sleep(1)
        print('semaphore is alive!')


def consume():
    print('Waiting for data!')
    item.append('item1')
    print('consume() got data!')
    semaphore.release()


t1 = threading.Thread(target=producer())
t2 = threading.Thread(target=consume())
t3 = threading.Thread(target=producer())

t1.start()
t2.start()
t3.start()
