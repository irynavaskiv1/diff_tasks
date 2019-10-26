def ask():
    while True:
        try:
            n = int(input("Enter a number: "))
        except:
            print("Please try again! \n ")
            continue
        else:
            break
        finally:
            print("all ok")

    print("Your multiply number is: ")
    print(n**2)

print(ask())


def enter_name():
    while True:
        try:
            a = int(input('Enter your number:'))
        except:
            print('It is not number!\n')
        else:
            break
    print('Your number is:')
    print(a)
enter_name()
