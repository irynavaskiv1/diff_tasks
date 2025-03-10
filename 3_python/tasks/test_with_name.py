print("I am "), __name__


def minmax(test, *args):
    res = args[0]
    for arg in args[1:]:
        if test(args, res):
            res = arg
    return res


def lessthan(x, y):
    return x < y


def grtrthan(x, y):
    return x > y


if __name__ == "__main__":
    print(minmax(lessthan, 4, 5))
    print(minmax(grtrthan, 3, 4))
