# create class without class statement

# 1. Example:
type('Ira', (), {'__init__': lambda self: self})


# 2. Example:
class Badik:

    counter = 2

    def __init__(self, breed):
        self.breed = breed

    def say_gav(self):
        return "Hi guys, my breed is " + self.breed


def Badik_init(self, breed):
    self.breed = breed


Badik2 = type('Badik2',
              (),
              {'counter': 2,
               '__init__': Badik_init,
               'say_gav': lambda self: "Hi, my brees is " + self.breed})

b = Badik('poroda')
print(b.say_gav())  # Hi guys, my breed is poroda

b2 = Badik2('poroda2')
print(b2.say_gav())  # Hi, my brees is poroda2
