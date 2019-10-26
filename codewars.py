def greet(name):
    ''' # Jenny has written a function that returns a greeting for a user.
    However, she's in love with Johnny, and would like to greet him
    slightly different.' She added a special case to her function, but she
    made a mistake.'''
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)


def greet1(name):
    return "Hello, my love!" if name == 'Johnny'\
        else "Hello, {name}!".format(name=name)


def number_to_string(num):
    '''Convert a Number to a String! '''
    return str(num)


def reverse(st):
    reversed('Hello World')
    reversed('Hi There.')
    print(st)


print('{2}, {0}, {1}'.format('a', 'v', 'd'))
print('Coordinates: {latitude}, {longitude}'.format(latitude='37.24N',
                                                    longitude='-115.81W'))
print('My name is: {name}, {surname}'.format(name="iryna", surname='vaskiv'))
print('My not full name is: {fullname[4]}, {fullsurname[3]}'.
      format(fullname="iryna", fullsurname="vaskiv"))
