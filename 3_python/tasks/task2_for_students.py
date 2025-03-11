def fibo(x):
    if x == 1:
        return 0
    elif x == 2:
        return 2
    return fibo(x - 1) + fibo(x - 2)


def palindrom(x):
    if len(x) <= 1:
        return True
    if x[0] != x[-1]:
        return False
    return palindrom(x[1:-1])


def fact(x):
    if x == 1:
        return 1
    return fact(x - 1) * x
