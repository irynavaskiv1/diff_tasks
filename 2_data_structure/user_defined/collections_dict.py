from collections import defaultdict
from collections import OrderedDict


d = defaultdict(int)
my_list = [1, 2, 3, 4, 2, 4, 1, 2]
for i in my_list:
    d[i] += 1
print(d)


# ---------------------------------------------------------------------------------------------------------------------

od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4

print('Before Deleting')
for key, value in od.items():
    print(key, value)

# deleting element
od.pop('a')
print('Before Deleting')
for key, value in od.items():
    print(key, value)

# Re-inserting the same
od['a'] = 1

print('\nAfter re-inserting')
for key, value in od.items():
    print(key, value)

simple_dict = {'a': 11, "b": 23}
simple_dict['d'] = 33
print(simple_dict)

