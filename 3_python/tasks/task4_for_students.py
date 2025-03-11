# 1. Read 10 symbols from file
f = open("test.txt", "w")
print(f.read(10))

# 2. Перемножити 2 lists
new_list = []
for x in [1, 2, 3]:
    for y in [3, 4, 6]:
        new_list.append(x * y)
print(f"{new_list} is new list!")

# 3. Перевірити чи є 1 в dict
d = {"my_key": 23, "my_key22": 23}
for key in d.keys():
    print(True if key == "my_key" else False)

# 4. Перемножити кожне  число в лісті
list_test = [1, 2, 4]
new_list2 = [list_test_item * 2 for list_test_item in list_test]
print(new_list2)

# 5. Забрати дублікати з істроки
test_str = "ssddffgghhjj"
"".join(set(test_str))
print(f"{test_str} is new_str!")
