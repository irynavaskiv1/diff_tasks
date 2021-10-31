class A:
    title = 'A'
    def __init__(self):
        print('class A')


class B(A):
    def __init__(self):
        print('class B')


class C(A):
    def __init__(self):
        print('class C')


class B1(B):
    def show_title(self):
        print(self.title)


class C1(C):
    def show_title(self):
        print(self.title)


class M:
    def show_title(self):
        print(self.title)


class B2(B, M):
    pass


class C2(C, M):
    pass


b1 = B1()
b1.show_title()

c1 = C1()
c1.show_title()
# є дублювання коду

b2 = B2()
b2.show_title()

c2 = C2()
c2.show_title()
