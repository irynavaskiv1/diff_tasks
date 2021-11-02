number = 9
result = 'number * number'
print(result)  # number * number

result1 = eval('number * number')
print(result1)  # 81


def calculatePerimeter(l):
    return 4*l


def calculateArea(l):
    return l*l


expression = input("Type a function: ")

for _ in range(1, 5):
    if expression == 'calculatePerimeter(l)':
        print("If length is ", _, ", Perimeter = ", eval(expression))
    elif expression == 'calculateArea(l)':
        print("If length is ", _, ", Area = ", eval(expression))
    else:
        print('Wrong Function')
        break
