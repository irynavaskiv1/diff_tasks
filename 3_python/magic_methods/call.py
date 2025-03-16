class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __call__(self, *args, **kwargs):
        print(" __call__ magic method ")


badik = Dog("Badik", age=1)
if callable(badik):
    badik("Callable Baadik: Hello")
