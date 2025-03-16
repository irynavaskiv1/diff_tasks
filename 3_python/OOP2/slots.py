class Limiter:
    __slots__ = ["age", "name", "job"]


x = Limiter()
# x.age # AttributeError: age

x.age = 24  # спочатку використати присвоєння, далі виклик
print(x.age)

# ____________________________________________________________________


class C:
    __slots__ = ["a", "b"]


y = C()
y.a = 1

# y.__dict__  AttributeError
print(getattr(y, "a"))  # 1

# ____________________________________________________________________


class D:
    __slots__ = ["a", "b", "__dict__"]


z = D()
print(z.__dict__)  # {}

# ____________________________________________________________________


class E:
    __slots__ = ["c", "d"]


class R(E):
    __slots__ = ["r", "m", "__dict__"]


c = R()
print(c.__dict__)  # {}
