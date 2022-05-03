import sys


def empty(): pass
a = empty()
b = empty()
print(sys.getrefcount(empty))  # 2

a = 1
print(sys.getrefcount(1))  # 748 --> interpreter works
