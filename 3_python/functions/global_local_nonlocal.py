# GLOBAL
x = 3


def function_global():
    print("x inside:", x)


# function_global()
# print("x outside:", x)

# LOCAL


def foo():
    y = "local"
    print(y)


# foo()


# LOCAL GLOBAL
x = "global "


def foo():
    global x
    y = "local"
    x = x * 2
    print(x)
    print(y)


# foo()

# LOCAL GLOBAL
x = 5


def foo():
    x = 10
    print("local x:", x)


# foo()
# print("global x:", x)

# NONLOCAL GLOBAL


def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)


print(x)
outer()
