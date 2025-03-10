def task1():
    """Виведіть на екран всі непарні значення, а також їхню суму з числової послідовності від 0 до 1000"""
    odd_values = []
    odd_values_sum = None
    try:
        range_list = list(range(0, 1000))
        odd_values = [i for i in range_list if i % 2 == 0]
        odd_values_sum = sum(odd_values)
        print(f"Odd values is {odd_values} !")
        print(f"Odd values sum is {odd_values_sum} !")
    except Exception as e:
        print("Exception in task1", e)

    return odd_values, odd_values_sum


print("\n")
task1()


def task2(start, pow2, number):
    """Виведіть на екран перші 20 елементів послідовності 2 4 8 16 32 64 128"""
    for i in range(0, number):
        curr_term = start * pow(pow2, i)
        print(curr_term, end=" ")


print("\n")
task2(2, 2, 20)


def task3(number):
    """
    Напишіть програму, яка пропонує користувачу ввести число від 1 до 12. Після введення числа програма повинна вивести
    на екран пору року до якої відноситься число яке ввів користувач. Також потрібно вивести на екран попередження з
    відповідною помилкою, якщо число не входить в діапазон від 1 до 12 або не є числом.
    :param number: int
    :return: int
    """
    if type(number) == int and number <= 12:
        try:
            weather = {
                1: "January",
                2: "February",
                3: "March",
                4: "April",
                5: "May",
                6: "June",
                7: "July",
                8: "August",
                9: "September",
                10: "October",
                11: "November",
                12: "December",
            }
            result = weather[number]
            print(result)
        except Exception as e:
            print("Error in task3, ", e)
    else:
        print(f"{number} is not number or is not numeric value!")


print("\n")
task3("111")
task3(111)
task3(1)
