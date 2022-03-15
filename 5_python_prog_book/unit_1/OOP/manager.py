from person import Person


class Manager(Person):
    """ """
    def give_raise(self, percent, bonus=0.1):
        self.pay *= (1.0 + percent + bonus)


if __name__ == '__main__':
    tom = Manager(name='Tom Tomuch', age=30, pay=3000, job='Manager')
    print(tom.last_name())
    tom.give_raise(.20)
    print(tom.pay)
