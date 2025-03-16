# check ids main idea of mutable / immutable

a = 3
a = 5
print("declarate a first time", id(a))  # 4520122480
print("declarate a second time", id(a))  # 4520122544

l = 260
l = 260
print("declarate l first time", id(l))  # 140305592999696
print("declarate l first time", id(l))  # 140305592999696

# after 255 int , id will not change
