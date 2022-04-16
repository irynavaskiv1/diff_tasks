class AGE:

    def __init__(self):
        self.fget = 'fget'
        self.fset = 'fset'
        self.fdel = 'fdel'

    def __get__(self, instance, owner):
        print('__get__')
        if instance is None:
            return self.fget
        else:
            return instance._age

    def __set__(self, instance, value):
        print('__set__')
        instance._age = value

    def __delete__(self, instance):
        print('__del__')
        if instance is None:
            raise AttributeError('Can not del attribute')
        else:
            del instance._age


class Vaskiv:

    def __init__(self, age):
        self._age = age
    age = AGE()


# get
v = Vaskiv('Iren Va')
print(v.age)

# set
v.age = 25

# delete
del v.age
