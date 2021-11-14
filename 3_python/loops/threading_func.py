import time
import threading

x = 0


def calculate_square(numbers):
    print('calculate square')
    print(threading.current_thread())
    for n in numbers:
        time.sleep(3)
        print('square is: ', n * n)


def calculate_cube(numbers):
    global x
    print('calculate cube')
    print(threading.current_thread())
    for n in numbers:
        time.sleep(3)
        print('cube is: ', n * n * n)
    x = 0


def monitoring():
    while True:
        time.sleep(0.5)
        print('monitor sleep: *** ')


args = [1, 2, 3, 4]
t = time.time()

t1 = threading.Thread(target=calculate_square, args=(args,), name='DoFirstThread', daemon=False)
t2 = threading.Thread(target=calculate_cube, args=(args,), name='DoSecondThread', daemon=False)
t3 = threading.Thread(target=monitoring, name='DoThirdThread', daemon=False)

t1.start()  # run immediately
t2.start()  # run immediately
t3.start()  # run immediately


time.sleep(10)
print('done in: ', time.time() - t)
print('I am done with all work!')
