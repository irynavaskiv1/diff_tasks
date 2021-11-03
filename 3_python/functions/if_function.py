def has_33(nums):
    for i in range(0, len(nums)-1):
        if nums[i] == 6 and nums[i+1] == 6:
            return True
    return False


print(has_33([6, 6, 8]))


def func_has_22(nums):
    for i in range(0, len(nums)-1):
        if nums[i] == 2 and nums[i+1] == 2:
            return True
    return False


print(func_has_22([2, 3, 4, 2, 2]))


def last_symbol(nums):

    for i in range(0, len(nums)+1):
        if nums[i:i+2] == [3, 5]:
            return True
    return False


print(last_symbol([5, 3, 5, 3]))


def iravaskiv4(a, b, c):
    if sum([a, b, c]) <= 21:
        return sum([a, b, c])


print(iravaskiv4(1, 2, 3))


def vaskiv(a, g):
    if sum([a, g]) <= 32:
        return sum([a, g])
    else:
        return "it is incorrect"


print(vaskiv(30, 40))


def udemy(a, b, c):
    if sum([a, b, c]) <= 21:
        return sum([a, b, c])
    elif 11 in [a, b, c] and sum([a, b, c])-10 <= 21:
        return sum([a, b, c])-10


print(sum([50, 60, 70]))
