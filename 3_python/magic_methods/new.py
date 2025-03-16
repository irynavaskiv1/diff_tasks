class Child:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Person:
    def __new__(cls, *args, **kwargs):  # create memory to object
        if kwargs.get("age") < 18:
            obj = object.__new__(Child)
            print("Child created")
        else:
            obj = super().__new__(cls)  # all classes has inheritance from object
            print("Person created")

        obj.__dict__  # {}
        obj.__class__.__dict__  # {'__module__': '__main__', '__new__': <staticmethod object at 0x7fcc09192580> .....
        return obj

    def __init__(self, name, age):
        self.name = name
        self.age = age


jon = Person("Jon", age=24)  # args: Jon kwargs: {'age': 24}
jon2 = Person(name="Jon2", age=16)  # args: () kwargs: {'name': 'Jon2', 'age': 24}
