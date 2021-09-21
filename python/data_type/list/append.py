
my_list = [1, 2, 3, 4, 5]

print(len(my_list))
print(my_list[:3])


my_list.append('append')
my_list.pop(0)
my_list.reverse()
print(my_list)

matrix = ([1, 2, 3], [4, 5, 6], [7, 8, 9])
first_fow = [first[0] for first in matrix]
print(first_fow)
