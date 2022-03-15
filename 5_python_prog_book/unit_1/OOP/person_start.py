class Person:
    def __init__(self, name, age, pay, job):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job


if __name__ == '__main__':
    bob = Person(name='Bob', age=30, pay=3000, job='Dev')
    sue = Person(name='Sue', age=20, pay=5000, job='QA')
    print(bob.name, sue.name)

    print(bob.name.split()[-1])
    sue.pay *= 1.4
    print('New Sue pay: ', sue.pay)
