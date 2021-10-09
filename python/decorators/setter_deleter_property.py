class Vaskiv:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @name.deleter
    def name(self):
        del self._name


ira = Vaskiv('Ira')
print(ira.name)

ira.name = 'Ira Vaskiv'
print(ira.name)  # without ira.name() use ira.name like property

del ira.name
