# є можливість імпортувати і запускати файл в stand alone форматі
class Person:

    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def last_name(self):
        return self.name.split()[-1]

    def giveRaise(self, persent):
        self.pay = int(self.pay * (1 + persent))

    def __str__(self):
        return '[Person: {}, {}]'.format(self.name, self.pay)


class Manager(Person):
    def giveRaise(self, persent, bonus=.10):
        # self.pay = int(self.pay * (1 + persent + bonus)) - неправильно -> копіпаст
        Person.giveRaise(self, persent + bonus)


if __name__ == '__main__':
    # тільки коли файл запускається для тестування
    bob = Person('Bob Smith', 'QA', 20000)
    sue = Person('Sue Jones', 'AQA', 25000)
    jak = Person('Jak', job='Dev', pay=40000)
    # print(bob)
    # print(sue)
    # print(bob.name, bob.job, bob.pay)
    # print(sue.name, sue.job, sue.pay)
    # print(jak.name, jak.job, jak.pay)

    print('----------------------------------')
    # print('Surname is ', bob.name.split()[-1])
    sue.pay *= 1.1
    # print('Sue new pay is ', round(sue.pay, 5))

    # print('----------------------------------')
    # print(bob.last_name(), sue.last_name())
    # print(sue.giveRaise(0.1))
    # print(sue.pay)
    # print(sue)

    print('----------------------------------')
    tom = Manager('Tom Jones', 'mng', 50000)
    tom.giveRaise(.20)
    print(tom.last_name())
    print(tom)

    print('-----All three-----')
    # поліморфізм, залежність методу giveRaise до об*єкта до якого він відноситься
    for obj in (bob, sue, tom):
        obj.giveRaise(.10)
        print(obj)

