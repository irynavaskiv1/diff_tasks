class MyClass:
    """Class Docstring"""

    MY_VAR = 10

    def method(self):
        self.__class__.MY_VAR = 20
        print("self.method.__name__", self.method.__name__)
        print("self.method.__doc__", self.method.__doc__)

        print("self.__class__.__name__", self.__class__.__name__)
        print("self.__class__.__doc__", self.__class__.__doc__)


m = MyClass()
m.method()
