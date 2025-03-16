# use magic method
a = [1, 2, 3]
b = (1, 2, 3)
print("a.__sizeof__():", a.__sizeof__())
print("b.__sizeof__():", b.__sizeof__())

# use method
d = dict.fromkeys(a)
d2 = dict.fromkeys(b)
print("d:", d)
print("d2:", d2)
