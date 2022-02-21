from abc import ABCMeta, abstractmethod


class Super(metaclass=ABCMeta):
    def delegate(self):
        self.action()

    @abstractmethod
    def action(self):
        pass


# ось тут ми не можемо створити інстанс класу Super x = Super() випаде помилка,
# бо ми оприділили абстрактний метод

class Sub(Super):
    def action(self):
        print('spam')

# тепер зможемо, бо ми дали реалізацію методу
