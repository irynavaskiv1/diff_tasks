class Dot:
    class_var_dot = 11

    def __init__(self, new_var):
        self.new_var = new_var


class Dot2(Dot):
    class_var_dot2 = 22

    def __init__(self, new_var2):
        self.new_var2 = new_var2


dot = Dot(".")
print(type(dot))

type(Dot)
print(isinstance(Dot, type))


body = """def __init__(self, new_var2):" \
       self.new_var2 = new_var2
       """
cls_dict = type.__prepare__("Dot2", (Dot,))
print(cls_dict)


exec(body, globals(), cls_dict)
print(cls_dict)

Dot2 = type("Dot2", (Dot,), cls_dict)
