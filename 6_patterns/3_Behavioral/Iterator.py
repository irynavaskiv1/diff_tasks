def iterate_first():
    alphabets = [chr(i) for i in range(65, 70)]
    for alpha in alphabets:
        print(alpha, end=" ")


def iterate_second():
    alphabets = [chr(i) for i in range(71, 120)]
    for alpha in alphabets:
        print(alpha, end=" ")


if __name__ == "__main__":
    iterate_first()
    print('\n')
    iterate_second()
