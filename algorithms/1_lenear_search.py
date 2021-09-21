def lenear_search(input_list, x):
    for i in range(len(input_list)):
        if input_list[i] == x:
            return i
    return -1


test_list = ['v', 'a', 's', 'k', 'i', 'v']
find_value = 'i'

print(lenear_search(test_list, find_value))
