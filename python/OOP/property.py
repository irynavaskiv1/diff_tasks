class MyClass:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    def full_name(self):
        return '{} {}'.format(self.name, self.last_name)

    def email(self):
        return '{}@globallogic'.format(self.full_name())

    @property
    def email_property(self):
        return '! {}@globallogic !'.format(self.full_name())\


    @email_property.setter
    def email_property(self):
        self.name = self.full_name().split()[0]
        self.last_name = self.full_name().split()[1]

    @email_property.deleter
    def email_property(self):
        return '{}@globallogic'.format(self.full_name())


empl1 = MyClass('Ira', 'Vaskiv')
empl2 = MyClass('Ira2', 'Vaskiv2')

print(empl1.email())
print(empl2.email_property)

print(empl2.full_name('Test'))
print(empl2.full_name('Test'))
print(empl2.full_name('Test'))
