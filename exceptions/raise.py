class MyBad:
    pass


def stuff():
    raise MyBad()


try:
    stuff()
except MyBad:
    print('got it')

#____________________________________________________

try:
    raise IndexError('spam')
except IndexError:
    print('jfjfjjfjf')
    raise

#____________________________________________________
