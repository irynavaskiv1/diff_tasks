class MyError(Exception):
    pass


def stuff(file=None):
    raise MyError()


my_file = open('data.txt', 'w')
try:
    stuff(file=my_file)
finally:
    my_file.close()
