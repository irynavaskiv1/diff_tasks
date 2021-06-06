def check(i):
    print("geeks")

    return i


print(10 > 11 > check(3))
print("\r")
print(10 < 11 > check(3))
print("\r")
print(10 < 11 > check(12))

#________________________________________________________________________


def check2(i):
    print("geeks")

    return i


print(all(check2(i) for i in [1, 1, 0, 0, 3]))
print("\r")
print(any(check2(i) for i in [0, 0, 0, 1, 3]))
