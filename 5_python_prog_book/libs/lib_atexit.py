import atexit


def bye():
    ''' bye function will be work after program will be close '''
    print('Bye!')


atexit.register(bye)
