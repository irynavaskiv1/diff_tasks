from classtools import AttrDisplay


class Person(AttrDisplay):
    """
    є можливість імпортувати і запускати файл в stand alone форматі
    створює і обробляє інформацію про людей
    """

    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def last_name(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __str__(self):
        return '[Person: {}, {}]'.format(self.name, self.pay)


class Manager(Person):
    """
    версія класу Person, адаптована в відповідності до вимог
    """

    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)

    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)


if __name__ == '__main__':
    # тільки коли файл запускається для тестування
    bob = Person('Bob Smith', 'QA', 20000)
    sue = Person('Sue Jones', 'AQA', 25000)
    jak = Person('Jak', job='Dev', pay=40000)
    print(bob)
    print(sue)
    print(bob.name, bob.job, bob.pay)
    print(sue.name, sue.job, sue.pay)
    print(jak.name, jak.job, jak.pay)

    print('----------------------------------')
    print('Surname is ', bob.name.split()[-1])
    sue.pay *= 1.1
    print('Sue new pay is ', round(sue.pay, 5))

    print('----------------------------------')
    print(bob.last_name(), sue.last_name())
    print(sue.giveRaise(0.1))
    print(sue.pay)
    print(sue)

    print('----------------------------------')
    tom = Manager('Tom Jones', 50000)
    tom.giveRaise(.20)
    print(tom.last_name())
    print(tom)

    print('-----All three-----')
    # поліморфізм, залежність методу giveRaise до об*єкта до якого він відноситься
    for obj in (bob, sue):
        obj.giveRaise(.10)
        print(obj)


class Department:
    def __init__(self, *args):
        self.members = list(args)

    def addMember(self, person):
        self.members.append(person)

    def giveRaise(self, percent):
        for person in self.members:
            person.giveRaise(percent)

    def showAll(self):
        for person in self.members:
            print(person)


# development = Department(bob)
# development.addMember(sue)
# development.giveRaise(0.10)
# development.showAll()
