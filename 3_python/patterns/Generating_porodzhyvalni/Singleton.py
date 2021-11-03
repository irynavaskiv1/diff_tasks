class Singleton:
    """
    Singleton it is a generating design pattern that ensures that the class has only one instance and
    provides a global access point to it.
    """

    obj = None  # attribute for storing a singe copy

    def __new__(cls, *args, **kwargs):
        if cls.obj is None:  # it will work once
            cls.obj = object.__new__(cls, *args, **kwargs)
        return cls.obj  # will return Singleton

    def __init__(self):
        print('_init__', type(self))


if __name__ == "__main__":

    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")
