class Property:

    def __init__(self, fget=None, fdel=None, fset=None, doc=None):
        self.fget = fget
        self.fdel = fdel
        self.fset = fset
        self.__doc__ = doc

    def __get__(self, instance, instancetype=None):
        if instance is None:
            return self
        if self.fget is None:
            raise AttributeError('can not get attribute')
        return self.fget(instance)

    def __set__(self, instance, value):
        if self.fset is None:
            raise AttributeError('can not set attribute')
        return self.fset(instance)

    def __del__(self, instance):
        if self.fdel is None:
            raise AttributeError('can not del attribute')
        return self.fdel(instance)


class Vaskiv:

    def getName(self):
        pass

    def setName(self, value):
        pass

    name = Property(getName(), setName())
