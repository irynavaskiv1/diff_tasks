import copy


class General:

    class Memento:
        def __init__(self, remember_value):
            self.remember_value = remember_value

        def get_first_value(self):
            return self.remember_value

    def set_value(self, value):
        print(f'General set value to {value} !')
        self.value = value

    def get_value(self):
        print(f'General get value {self.value} !')

    def save_value(self):
        print(f'General save value !')
        return self.Memento(copy.deepcopy(self))

    def get_remember_value(self, memento):
        self = memento.get_first_value()
        print(f'General get old value {self.value} !')


if __name__ == '__main__':
    general = General()
    general.set_value(1)
    general.get_value()
    general.set_value(2)
    general.get_value()
    remember_value = general.save_value()
    general.set_value(3)
    general.get_value()
    general.get_remember_value(remember_value)
