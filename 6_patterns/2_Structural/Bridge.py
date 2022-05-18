from abc import ABCMeta, abstractmethod


class MainAbstraction(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def to_do_method(*args):
        pass


class RefinedAbstractionFirst(MainAbstraction):

    def __init__(self, implementer):
        self.implementer = implementer

    def to_do_method(self, *args):
        self.implementer.to_do_method(*args)


class RefinedAbstractionSecond(MainAbstraction):

    def __init__(self, implementer):
        self.implementer = implementer

    def to_do_method(self, *args):
        self.implementer.to_do_method(*args)


class MainImplementer(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def to_do_method(*args: tuple) -> None:
        pass


class ConcreteImplementerFirst(MainImplementer):

    @staticmethod
    def to_do_method(*args: tuple) -> None:
        print(args)


class ConcreteImplementerSecond(MainImplementer):

    @staticmethod
    def to_do_method(*args: tuple) -> None:
        for arg in args:
            print(arg)


main_abstraction_a = RefinedAbstractionFirst(ConcreteImplementerFirst)
main_abstraction_a.to_do_method('i', 'r', 'a')  # ('i', 'r', 'a')
main_abstraction_b = RefinedAbstractionSecond(ConcreteImplementerSecond)
main_abstraction_b.to_do_method('i', 'r', 'a')  # i r a
