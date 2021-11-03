                                         # abs()
# print('Absolute value of -100 is:', abs(-100))
# print('Absolute value of -30.33 is:', abs(-30.33))

                                         # any()
# True since 1,3 and 4 (at least one) is true
l = [1, 3, 4, 0]
# print(any(l))

# False since both are False
l = [0, False]
# print(any(l))

# True since 5 is true
l = [0, False, 5]
# print(any(l))

# False since iterable is empty
l = []
# print(any(l))

                                         # all()
# all values true
l = [1, 3, 4, 5]
# print(all(l))

# all values false
l = [0, False]
# print(all(l))

# one false value
l = [1, 3, 4, 0]
# print(all(l))

# one true value
l = [0, False, 5]
# print(all(l))

# empty iterable
l = []
# print(all(l))


                                         # ascii()
normalText = 'Python is interesting'
# print(ascii(normalText))

otherText = 'Pythön is interesting'
# print(ascii(otherText))

# print('Pyth\xf6n is interesting')

                                        # bin()
number = 5
# print('The binary equivalent of 5 is:', bin(number))

                                         # bytearray()
string = "Python is interesting."
# string with encoding 'utf-8'
arr = bytearray(string, 'utf-8')
# print(arr)

                                         # callable()
x = 5
# print(callable(x))


def testFunction():
    print("Test")


y = testFunction
# print(callable(y))

                                         # bytes()
string = "Python is interesting."
# string with encoding 'utf-8'
arr = bytes(string, 'utf-8')
# print("arr", arr)

                                         # bytes()
# print(chr(97))
# print(chr(65))
# print(chr(1200))

                                         # compile()
codeInString = 'a = 5\nb=6\nsum=a+b\nprint("sum =",sum)'
codeObejct = compile(codeInString, 'sumstring', 'exec')
# exec(codeObejct)

                                         # dict()
# keyword argument is not passed
numbers1 = dict([('x', 5), ('y', -5)])
# print('numbers1 =', numbers1)

# keyword argument is also passed
numbers2 = dict([('x', 5), ('y', -5)], z=8)
# print('numbers2 =', numbers2)

# zip() creates an iterable in Python 3
numbers3 = dict(dict(zip(['x', 'y', 'z'], [1, 2, 3])))
# print('numbers3 =', numbers3)

                                         # dir()
number = [1, 2, 3]
# print(dir(number))

# print('\nReturn Value from empty dir()')
# print(dir())

                                         # enumerate()
grocery = ['bread', 'milk', 'butter']
enumerateGrocery = enumerate(grocery)

# print(type(enumerateGrocery))

# converting to list
# print(list(enumerateGrocery))

# changing the default counter
enumerateGrocery = enumerate(grocery, 10)
# print(list(enumerateGrocery))

                                         # globals()
age = 23
# print('The age is:', age)

globals()['age'] = 25
# print('The age is:', age)

                                         # sorted()
# vowels list
py_list = ['e', 'a', 'u', 'o', 'i']
# print(sorted(py_list))

# string
py_string = 'Python'
# print(sorted(py_string))

# vowels tuple
py_tuple = ('e', 'a', 'u', 'o', 'i')
# print(sorted(py_tuple))

                                         # memoryview()
# random bytearray
random_byte_array = bytearray('ABC', 'utf-8')

mv = memoryview(random_byte_array)

# access memory view's zeroth index
# print(mv[0])

# create byte from memory view
# print(bytes(mv[0:2]))

# create list from memory view
# print(list(mv[0:3]))

                                         # zip()
number_list = [1, 2, 3]
str_list = ['one', 'two', 'three']

# No iterables are passed
result = zip()

# Converting iterator to list
result_list = list(result)
# print(result_list)

# Two iterables are passed
result = zip(number_list, str_list)

# Converting iterator to set
result_set = set(result)
# print(result_set)
