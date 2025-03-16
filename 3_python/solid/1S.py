"""
Single responsibility principle - Кожен об'єкт має виконувати лише один обов'язок. Клас має виконувати 1 дію.
"""


class IraName:
    def __init__(self, name):
        self.name = name

    def return_name(self):
        return self.name


class IraSurname:
    def __init__(self, surname):
        self.surname = surname

    def get_surname(self):
        return self.surname


n = IraName("irynka-kanfetka")
print(n.return_name())

m = IraSurname("va")
print(m.get_surname())
