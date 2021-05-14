class MixedNames:
    data = 'spam'

    def __init__(self, value):
        self.data = value

    def display(self):
        print(self.data, MixedNames.data)


m = MixedNames(1)
m.display()

n = MixedNames(2)
n.display()
