class MyError(Exception):
    pass


def stuff(file=None):
    raise MyError()


file = open('data.txt', 'w')
try:
    stuff(file=file)
finally:
    file.close()
