import time
from collections import deque


def mygen(income, c=1):
    counter = c
    for i in income:
        if i:
            yield counter, i
            print('One more yield call')
            counter += 1


def count_task(n, name):
    for i in range(n+1):
        print(f'Action of generator {name}')
        yield i
        time.sleep(0.3)


gen1 = count_task(3, 1)
gen2 = count_task(2, 2)
gen3 = count_task(1, 3)


task = deque(gen1, gen2, gen3)
