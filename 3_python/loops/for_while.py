start = 0
finish = 10
while start < finish:
    print(start, end=" ")
    start += 1
else:
    print("the end")


# написати від 10 до 0

start = 10
finish = 0
while start > finish:
    print(start, end=" ")
    start -= 1
    continue
else:
    print("end")

for i in [0, 2, 3, 4, 5]:
    print(i)
else:
    print(i, "is the last")


print(range(0, 10, 2))


# приклади з класної роботи

for var in "string":
    if var == "s":
        continue
    print(var)
else:
    print("the end")


for i in "vaskiv":
    if i == "v":
        continue
    print(i)
else:
    print("the end")


for var in "string":
    if var == "s":
        print(var)
        break
else:
    print("the end")


for var in "vaskiv":
    print(var * 2, end=" ")


my_list = [1, 3, 45, 6, 7]
for var in my_list:
    print(var + 2, end=" ")

iras_list = [1, 4, 56.9, 2]
i = 0
for var in iras_list:
    iras_list[i] = var + 2
    i += 1
print(iras_list)

d = {1: "one", 2: "two", 3: "tree", 4: "four"}
for key in d:
    d[key] += "1"
print(d)

my_list = [1, 2, 4, 5, 67]
i = 0
while i < len(my_list):
    my_list[i] += 10
    i += 1
print(my_list)

# до кожного елементу додати 10
iras_list = [23, 45, 56.9, 56]
i = 0
while i < len(iras_list):
    iras_list[i] += 10
    i += 1
print(iras_list)


iras_list = [23, 45, 56.9, 56]
i = 0
for var in iras_list:
    iras_list[i] += var + 10
print(iras_list)


vaskiv_list = [1, 3, 4.5, 6]
i = 0
while i < len(vaskiv_list):
    vaskiv_list[i] += 10
    i += 1
print(vaskiv_list)


test_list = [23, 45, 76, 68]
for i in test_list:
    i += 1
    print(i * 2, end=" ")

test_list2 = [23, 45, 76, 68]
i = 0
for var in test_list2:
    test_list2[i] += 10
    i += 1
print(test_list2)

test_list3 = [23, 45, 46, 68]
i = 0
while i < len(test_list3):
    test_list3[i] += 10
    i += 1
print(test_list3)

test_list = [23, 45, 46, 68, 23, 34]
print(list(range(len(test_list))))
print(list(range(len(test_list))))

test_list9 = [1, 34, 5.6, 6, 677]
i = 0
for i in range(len(test_list9)):
    test_list9[i] += 2
    print(i, test_list9[i])

fruit = ["banana", "apple"]
for var in fruit:
    print("i love", var)

i = 0
for i in range(len(fruit)):
    print("i love", fruit[i])


for x in 1, 3, 4:
    print(x**2, end=" ")
