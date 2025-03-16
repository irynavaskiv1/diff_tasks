import pprint


class MyMeta(type):
    class_var = 20

    def __new__(cls, class_name, bases, class_dict):
        if len(bases) > 1:
            raise TypeError(f"Can not  {class_name}")
        cls_obj = super().__new__(cls, class_name, bases, class_dict)
        return cls_obj

    def __init__(self, *args, **kwargs):
        super.__call__(*args, **kwargs)

    def run(self):
        print(f"С: Run {self}", self.obj_var)

    @property
    def attr(self):
        return "Class attribute"

    @classmethod
    def cls_method(cls):
        return "Class method"


class MyClass(metaclass=MyMeta):
    obj_var = 30

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, param):
        self.param = param

    def run(self):
        print(f"O: Run {self}")


inst = MyClass(1001)
inst.run()

pprint(inst.__dict__)
pprint(MyClass.__dict__)
pprint(MyMeta.__dict__)
