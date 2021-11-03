class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __call__(self, *args, **kwargs):
        print('Hello')


badik = Dog('Badik', age=1)
if callable(badik):
    badik("hello")
