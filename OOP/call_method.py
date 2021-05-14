class Foo(object):
    def __init__(self, x, y=0):
        self.x = x
        self.y = y


print(Foo.__class__)  # <class 'type'>
f = Foo(1, y=2)
