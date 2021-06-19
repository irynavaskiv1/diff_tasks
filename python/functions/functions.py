import unittest


def dog_check(mystring):
    if 'dog' in mystring:
        return True
    else:
        return False


dog_check('dog')


class myfunction():

    def func(*args):
        for item in args:
            print(item)
    func(2, 4)


def myfunction2(**jelly):
    print(jelly)


myfunction2(name='ira', surname='vaskiv')


def myfunction3(*args, **kwargs):
    print(args)
    print(kwargs)
    print('i like {} {}'.format(args[0], kwargs["name"]))


myfunction3(2, 4, name='ira', surname='vaskiv')


def animal_crackers(text):
    animal = text.split()
    first = animal[0]
    second = animal[0]

    return first[0] == second[0]


def makes_twenty(*args):
    return [a for a in args if a % 2 == 0]


print(makes_twenty(10.1, 30))


def myfunction4(*args):
    return [a for a in args if a*3 == 30]


print(myfunction4(10, 2, 4, 10,  5))


def myfunction5(*args):
    return [n for n in args if n % 2 == 0]


print(myfunction5(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


def myfunction6(**kwargs):
    for key, value in kwargs.items():
        print("Surname for {} is {}".format(key, value))


myfunction6(ira="vaskiv", marta="hfhfhfhf", petja="skdslkd")


def print_values(**kwargs):
    for key, value in kwargs.items():
        print("The value of {} is {}".format(key, value))


print_values(
            name_1="Alex",
            name_2="Gray",
            name_3="Harper",
            name_4="Phoenix",
            name_5="Remy",
            name_6="Val"
        )


def amount(*args):
    return (a for a in args if a * 3 == 9)


print(amount(1, 3, 45, 67, 8))


def old_macdonald(name):
    first_half = name[:3]
    second_half = name[3:]
    return first_half.capitalize() + second_half.capitalize()


print(old_macdonald('macdonald'))


def iravaskiv1(name):
    names = name[:5]
    surname = name[6:]
    return names.capitalize() + surname.capitalize()


print(iravaskiv1("iryna vaskiv"))


def master_yoga(text):
    wordlist = text.split()
    reverse_wordlist = wordlist[::-1]
    return reverse_wordlist


print(master_yoga('We are ready'))


def iravaskiv2(text):
    wordlist = text.split()
    change_wordlist = wordlist[::1]
    return change_wordlist


print(iravaskiv2('I think positive all day'))


def summer_69(arr):

    total = 0
    add = True

    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
                break

        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total


print(summer_69([1, 3, 5]))


def spy_game(nums):

    code = [0, 0, 7, 'x']

    for num in nums:
        if num == code[0]:
            code.pop(0)

    return len(code) == 1


print(spy_game([1, 2, 4, 0, 0, 7, 5]))


def count_primes(num):

    if num < 2:
        return 0

    primes = [2]
    x = 3

    while x <= num:
        for y in range(3, x, 2):
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2

    print(primes)
    return len(primes)


print(count_primes([100]))


def splicer(mystring):
    if len(mystring) % 2 == 0:
        return "EVEN"
    else:
        return mystring[0]


print(splicer(['Andy', 'Eve', 'Sally']))


names = ['Andy', 'Eve', 'Sally']
list(map(splicer, names))


def square(num):
    return num ** 2


print(square(3))


def check_even(num):
    return num % 2 == 0


print(check_even(8))


# check_even = lambda num: num%2 == 0
# print(check_even(8))

mynums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(lambda num: num % 2 == 0, mynums)))

names = ['Ira', 'Taras', 'Maria']
print(list(map(lambda x: x[::-1], names)))


# функція яка перемножує значення (записати)
def multiply(numbers):
    total = numbers[0]
    for x in numbers:
        total *= x
    return total


print(multiply([9, -3, 4]))


# тік так гра хрестик нолик
# from IPython.display import clear_output


def display_board(board):

    print(board[7] + '|' + board[8] + '|' + board[9])
    print('------')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('------')
    print(board[1] + '|' + board[2] + '|' + board[3])


test_board = ['#', 'X', 'O'', X', 'O', 'X', 'O', 'X', 'O', 'X']
display_board(test_board)


class Dog:

    def __init__(self, dogbreed, dogname):
        self.breed = dogbreed
        self.name = dogname


class Cat:

    def __init__(self, ownercat):
        self.owners = ownercat


my_cat = Cat(ownercat='ira')
print(my_cat.owners)


class Circle:
    pi = 3.14

    def __init__(self, radius=3):
        self.radius = radius

    def get_circle(self):
        return self.radius * self.pi * 3


my_circle = Circle()
print(my_circle.get_circle())


# наслідування
class Animal():

    def __init__(self):
        print('ANIMAL CREATED')

    def who_am_i(self):
        print("I am an animal")

    def eating(self):
        print('I can eating')


class Dog2(Animal):

    def __init__(self):
        Animal.__init__(self)
        print('Dog created')

    def who_am_i(self):
        print("I am Dog")


mydog = Dog2()
mydog.who_am_i()


# поліморфізм
class Dog3():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says woof!"


class Cat():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says meow"


niko = Cat("Niko")
felix = Dog("Felix")

# print(felix.speak())
print(niko.speak())

for pet in [niko, felix]:
    print(type(pet))
    print(type(pet.speak()))


def pet_speak(pet):
    print(pet.speak)


pet_speak(niko)
# pet_speak(felix)


# special methods
class Book:

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages


b = Book('Python roks', 'Jose', 200)
print(b)


class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1, x2 = self.coor1
        y1, y2 = self.coor2
        return ((x2-x1)**2 + (y2-y1)**2)**0.5

    def slope(self):
        x1, x2 = self.coor1
        y1, y2 = self.coor2
        return ((y2-y1)/(x2 - x1))

    def somethink(self):
        x1, x2 = self.coor1
        y1, y2 = self.coor2
        return (x1+x2+y1+y2)


coordinate1 = (3, 1)
coordinate2 = (8, -10)

li = Line(coordinate1, coordinate2)

print(li.distance())
print(li.slope())
print(li.somethink())


class Sample:

    def __init__(self, value):
        self.value = value

    def add_to_value(self, amount):
        self.value = self.value + amount
        print('We just add {}'.format(amount))


myobj = Sample(300)
print(myobj.value)
print(myobj.add_to_value(400))


def add(n1, n2):
    print(n1+n2)


add(10, 20)


class exception1:
    try:
        f = open('testfile', 'r')
        f.read()
    except Exception:
        print('This is a exeption')

    finally:
        print('i write without exeptions')


def ask_for_int():
    while True:
        try:
            input('Please provide name: ')
        except Exception:
            print('Whoops! That is not a mane')
            continue
        else:
            print('Yes, thank you')
            break
        finally:
            # print('End or blocks')
            print('Great work Iryna')


ask_for_int()

try:
    x = 5
    y = 1
    z = x/y
except Exception:
    print("Error")
finally:
    print("All done!")


class TestCap(unittest.TestCase):

    def test_one_world(self):
        text = 'python'
        result = cap.cap_text(text)
        self.assertEquals(result, 'Python')

    def test_multiple_words(self):
        text = 'monty python'
        result = cap.cap_text(text)
        self.assertEquals(result, 'Monty Python')


if __name__ == '__main__':
    unittest.main()


def func():
    return 1


print(func())


def hello():
    return('Hello')


print(hello())

greet = hello()
print(greet)


def hello(name="Jose"):
    print('The hello() function has been executed!')

    def greet():
        return '\t This is the greet() func inside hello!'

    print(greet())

    def ira():
        int(input('Hello enter name'))
    print(ira())


print(hello())


def create_cubes(n):
    result = []
    for x in range(n):
        result.append(x**3)
    return result


print(create_cubes(10))


def create_cubes(n):
    for x in range(n):
        yield x**3


print(create_cubes(10))
