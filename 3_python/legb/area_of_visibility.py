X = 11  # global name inside module


def f():
    print("def f x=", X)


def g():
    X = 22
    print("def g x=", X)


class C:
    X = 33

    def m(self):
        X = 44
        self.X = 55


if __name__ == "__main__":
    print(X)
    f()
    g()
    print(X)

    obj = C()
    print("obj.X", obj.X)
    print("obj.C.X", C.X)
