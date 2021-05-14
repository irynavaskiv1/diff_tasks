class Singleton:
    obj = None  # attribute for storing a singe copy

    def __new__(cls, *args, **kwargs):
        print(type(cls))
        if cls.obj is None: # it will work once
            print('creating an object')
            cls.obj = object.__new__(cls, *args, **kwargs)
        return cls.obj # will return Singleton

    def __init__(self):
        print('_init__', type(self))


s1 = Singleton()
print()
s2 = Singleton()

# <class 'type'>
# creating an object
# _init__ <class '__main__.Singleton'>
#
# <class 'type'>
# _init__ <class '__main__.Singleton'>
