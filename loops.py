class loops:
    mystring = "Iryna Vaskiv"

    for letter in mystring:
        if letter != 'a':
            continue
        print(letter)


class loopsnumber:
     x=0

     while x<9:
         if x == 3:
           break
         print(f"The {x} is number")
         x=x+1


class loop:
    word = 'abcd'

    for index,letter in enumerate(word):
        print(index, letter)


index_count = 0

for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count,letter))

list1 = [1, 3, 4, 5, 6]
list2 = ['a', 'd', 'f', 'g', 'k']
list3 = ['df', 'fd', 'ff', 'dd', 'f']


mystring = 'Hello'
mylist = []

for letter in mystring:
    mylist.append(letter)
    print(mylist)

mylist =[x**2 for x in range(0, 11) if x%2 == 0]
print(mylist)

mylist = []
for x in [2, 3, 4, 5]:
    for y in [0, 8, 1, 6]:
        mylist.append(x*y)
print(mylist)
