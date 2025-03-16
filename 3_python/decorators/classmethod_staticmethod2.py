class Methods:
    def imeth(self, x):
        print(self, x)

    def smeth(x):
        print(x)

    def cmeth(cls, x):
        print(cls, x)

    smeth = staticmethod(smeth)  # same like @staticmethod
    cmeth = classmethod(cmeth)  # same like @classmethod
