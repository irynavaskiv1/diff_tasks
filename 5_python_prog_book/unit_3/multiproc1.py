import multiprocessing

input_data_list1 = [30, 40, 50]
input_data_list2 = [30, 40, 50, 60]


def multiply_list(input_list):
    result = 1
    for i in input_list:
        result = result * i
    print(f'multiply_list: {result}')


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=multiply_list, args=(input_data_list1,))
    p2 = multiprocessing.Process(target=multiply_list, args=(input_data_list2,))
    p2.daemon = True

    p1.start()
    p2.start()

    p1.join()
    p2.join()
