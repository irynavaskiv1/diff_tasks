import multiprocessing
import time

args = [1, 2, 3, 4]
var = 1, 2, 3, 4
t = time.time()


def calculate_square(numbers):
    print('calculate square')
    global var
    for n in numbers:
        time.sleep(3)
        print('square is: ', n * n)
        var = 10


def calculate_cube(numbers):
    global var
    print('calculate cube')
    for n in numbers:
        time.sleep(3)
        print('cube is: ', n * n * n)
        break


def monitoring():
    while True:
        time.sleep(0.5)
        print('monitor sleep: *** ')


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=calculate_square, args=(args,))
    p2 = multiprocessing.Process(target=calculate_cube, args=(args,))
    p2.daemon = True

    time.perf_counter()
    p1.start()
    p2.start()

    p1.join()
    p2.join()
    p1.terminate()
    print(p1.exitcode)
    print(p1.pid)
    print(p2.pid)

    time.sleep(10)
    print('done in: ', time.time() - t)
    print('I am done with all work!')
