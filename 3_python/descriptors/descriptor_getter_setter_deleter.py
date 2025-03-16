class DescSquare:
    def __init__(self, value):
        self.value = value

    def __get__(self, instance, cls):
        return self.value * 2

    def __set__(self, instance, value):
        if not isinstance(value, str) and len(value) < 3:
            raise TypeError("Expected type str with len 3 symbols!")
        self.value = value

    def __delete__(self, instance):
        instance.__dict__[self.value] = ""
        print("Delete ", self.value)


class Client1:
    x = DescSquare(3)


class Client2:
    x = DescSquare(10)


c1 = Client1()
c2 = Client2()

print(c1.x)  # 3 * 2
print(c2.x)  # 10 * 2


class NewClass:
    value = DescSquare("val")

    def __init__(self, value):
        self.value = value


book = NewClass("bad")
print(book.value)
del book.value
