class Count:
    def __init__(self, mymin, mymax):
        self.mymin = mymin
        self.mymax = mymax


obj1 = Count(1, 10)
print(obj1.mymin)  # 1
print(obj1.mymax)  # 10
print(obj1.mycurrent)  # AttributeError: 'Count' object has no attribute 'mycurrent'


class Count:
    def __init__(self, mymin, mymax):
        self.mymin = mymin
        self.mymax = mymax

    def __getattr__(self, item):
        self.__dict__[item] = 0
        return 0


obj1 = Count(1, 10)
print(obj1.mymin)  # 1
print(obj1.mymax)  # 10
print(obj1.mycurrent1)  # 0


class Count(object):
    def __init__(self, mymin, mymax):
        self.mymin = mymin
        self.mymax = mymax
        self.current = None

    def __getattr__(self, item):
        self.__dict__[item] = 0
        return 0

    def __getattribute__(self, item):
        if item.startswith("cur"):
            raise AttributeError
        return object.__getattribute__(self, item)
        # return super().__getattribute__(item)


obj1 = Count(1, 10)
print(obj1.mymin)  # 1
print(obj1.mymax)  # 10
print(obj1.current)  # 0
