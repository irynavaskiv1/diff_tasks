from abc import ABCMeta
from abc import abstractmethod

import copy


class Meta_Class(metaclass=ABCMeta):

    def __init__(self):
        self.id = None
        self.type = None

    @abstractmethod
    def course(self):
        pass

    def get_type(self):
        return self.type

    def get_id(self):
        return self.id

    def set_id(self, sid):
        self.id = sid

    def clone(self):
        return copy.copy(self)


class Subclass_1(Meta_Class):
    def __init__(self):
        super().__init__()
        self.type = "Data Structures and Algorithms"

    def course(self):
        print("Inside Subclass_1::course() method")


class Subclass_2(Meta_Class):
    def __init__(self):
        super().__init__()
        self.type = "Software Development Engineer"

    def course(self):
        print("Inside Subclass_2::course() method.")


# class - Subclass_3 Course
class Subclass_3(Meta_Class):
    def __init__(self):
        super().__init__()
        self.type = "Standard Template Library"

    def course(self):
        print("Inside Subclass_3::course() method.")


class Meta_Class_Cache:
    # cache to store useful information
    cache = {}

    @staticmethod
    def get_course(sid):
        COURSE = Meta_Class_Cache.cache.get(sid, None)
        return COURSE.clone()

    @staticmethod
    def load():
        subclass_2 = Subclass_2()
        subclass_2.set_id("1")
        Meta_Class_Cache.cache[subclass_2.get_id()] = subclass_2

        subclass_1 = Subclass_1()
        subclass_1.set_id("2")
        Meta_Class_Cache.cache[subclass_1.get_id()] = subclass_1

        subclass_3 = Subclass_3()
        subclass_3.set_id("3")
        Meta_Class_Cache.cache[subclass_3.get_id()] = subclass_3


# main function
if __name__ == '__main__':
    Meta_Class_Cache.load()

    Subclass_2 = Meta_Class_Cache.get_course("1")
    print(Subclass_2.get_type())

    Subclass_1 = Meta_Class_Cache.get_course("2")
    print(Subclass_1.get_type())

    Subclass_3 = Meta_Class_Cache.get_course("3")
    print(Subclass_3.get_type())
