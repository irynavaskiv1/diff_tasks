f = open('/home/iryna/Desktop/test2.txt', 'r+')
f.write('hello Iryna')
print(f.read())


def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)
