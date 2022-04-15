class Super:

    def method(self):
        print('in Super.method')

    def delegate(self):
        self.action()


class Inheritor(Super):
    """ наслідуємо методи, такі які вони є"""
    pass


class Replacer(Super):
    """повністю замінює Super.method"""
    def method(self):
        print('in Replacer.method')


class Extender(Super):
    """ розширюємо поведінку метода method"""
    def method(self):
        print('starting Extender.method')
        Super.method(self)
        print('ending Extender.method')


class Provider(Super):
    """ реалізовуємо необхідних метод"""
    def action(self):
        print('in Provider.action')


if __name__ == '__main__':
    for each_сlass in (Inheritor, Replacer, Extender):
        print('\n' + each_сlass.__name__ + '...')
        each_сlass().method()
    print('\nProvider...')
    x = Provider()
    x.delegate()
"""
Inheritor...
in Super.method

Replacer...
in Replacer.method

Extender...
starting Extender.method
in Super.method
ending Extender.method

Provider...
in Provider.action
"""
