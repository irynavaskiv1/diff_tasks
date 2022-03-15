class Person:
    def __init__(self, name, age, pay, job):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job

    def last_name(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        self.pay *= (1.0 + percent)


if __name__ == '__main__':
    bob = Person(name='Bob Smith', age=30, pay=3000, job='Dev')
    sue = Person(name='Sue Jones', age=20, pay=5000, job='QA')
    print('bob.name ', bob.name)
    print('sue.pay ', sue.pay)

    print('bob.last_name', bob.last_name())
    sue.give_raise(0.1)
    print('New Sue pay: ', sue.pay)
