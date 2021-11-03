# 1
def func(x, a=[]):
    a.append(x)
    print(a)


func(2)
func(3, [1, 2])
func(5)

# [2]
# [1, 2, 3]
# [2, 5]

# 2 Delete all elem from list
lst = [12, 3]
del lst[:]

# 3 Merge two dics
one = {"1": 'one', "3": 'three'}
two = {"2": 'two', "4": 'four'}
three = dict(one, **two)
print(three)
#  {'1': 'one', '3': 'three', '2': 'two', '4': 'four'}
