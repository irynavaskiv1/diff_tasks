# 1. Check if list contains integer x
l = [1, 2, 3]
print(1 in l)


# 2. Get missing number in sorted list
def get_missing_number(test_list):
    result = None
    for i in test_list:
        if not ((i + 1) - i != 1):
            result = i - 1
    return result


l1 = [1, 2, 3, 4, 5]
print(get_missing_number(l1))


# 3. Find duplicate number in integer list
def find_duplacates(elements):
    duplicates, seen = set(), set()
    for element in elements:
        if element in seen:
            duplicates.add(element)
        seen.add(element)
    return list(duplicates)


l2 = [1, 2, 3, 3, 4, 5, 5, 6, 7, 8, 8]
find_duplacates(l2)


# 4. Check if two strings are anagrams
def is_anagrams(str1, str2):
    return set(str1) == set(str2)


print(is_anagrams('кіт', 'тік'))
print(is_anagrams('кіт', 'так'))


# 5. Find max and min value in unsorted list
l3 = [1, 3, 4, 6, 3, 4, 0, 45]
print(max(l3))
print(min(l3))


# 6. Reverse string using recursion
def reverse(test_str):
    if len(test_str) <=1:
        return test_str
    return reverse(test_str[1:]) + test_str[0]


print(reverse('iravaskiv'))


# 7. Compute the first 10 fibonacci numbers
a, b = 0, 1
n = 10
for i in range(n):
    print(b)
    a, b = b, a+b


# 8. Check if string is palindrome
def is_palindrome(phrase):
    return phrase == phrase[::-1]


print(is_palindrome('anna'))
print(is_palindrome('ira'))

# 9. Use list as stack, array, queue
l4 = [1, 2, 3, 4]
l4 += [33, 45]

# as a stack
l4.append(10)
l4.pop()

# as a queue
l4.insert(5, 6)
l4.pop()
