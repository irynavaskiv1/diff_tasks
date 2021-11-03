from python.OOP.person import Person


class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)

    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)

    def __getattr__(self, attr):
        return getattr(self.person, attr)

    def __str__(self):
        return str(self.person)


if __name__ == '__main__':
    bob = Person('Bob Smith', 'QA', 20000)
    sue = Person('Sue Jones', 'AQA', 25000)
    tom = Manager('Tom Jones', 25000)

    print('-----All three-----')
    for obj in (bob, sue, tom):
        obj.giveRaise(.10)
        print(obj)
