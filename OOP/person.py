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




if __name__ == '__main__':
    # тільки коли файл запускається для тестування
    bob = Person('Bob Vaskiv')
    sue = Person('Sue Vaskiv1', 'QA', 25)
    jak = Person('Jak', job='Dev', pay=40)
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
