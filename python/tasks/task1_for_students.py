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


l = [1, 2, 3, 4, 5]
print(get_missing_number(l))


# 3. Find duplicate number in integer list
def find_duplacates(elements):
    duplicates, seen = set(), set()
    for element in elements:
        if element in seen:
            duplicates.add(element)
        seen.add(element)
    return list(duplicates)


l = [1, 2, 3, 3, 4, 5, 5, 6, 7, 8, 8]
find_duplacates(l)


# 4. Check if two strings are anagrams
def is_anagrams(str1, str2):
    return set(str1) == set(str2)


print(is_anagrams('кіт', 'тік'))
print(is_anagrams('кіт', 'так'))
