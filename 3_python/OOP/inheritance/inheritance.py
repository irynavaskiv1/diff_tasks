class ParentClass:
    DEFAULT_VAR = 5

    def __init__(self):
        self.title = "IRA"

    def parent_method(self):
        print(self.parent_method.__name__)

    def hello(self):
        print(f"Hello from {self.__class__.__name__}")


class SubClass(ParentClass):
    def __init__(self):
        self.title = "IRASUB"

    def show_value(self):
        print(self.DEFAULT_VAR)

    def hello(self):
        print(f"Hello from {self.__class__.__name__}")


class SubClass2(SubClass):
    def __init__(self):
        self.title = "IRASUB2"

    def show_value(self):
        print(self.DEFAULT_VAR)

    def hello(self):
        print(f"Hello from {self.__class__.__name__}")


# дерево наслідування, від чого наслідується клас
print(SubClass.__mro__)
# (<class '__main__.SubClass2'>, <class '__main__.SubClass'>, <class '__main__.ParentClass'>, <class 'object'>)

# дерево наслідування, які класи наслідуються від класу
print(SubClass.__subclasses__())

s = SubClass2()
print(super(SubClass2, s))
