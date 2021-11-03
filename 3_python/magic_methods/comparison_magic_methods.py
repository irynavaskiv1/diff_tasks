class DogBig:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __int__(self):
        return self.age


class DogSmall:
    """
    # methods for comparison with a regular int or float:
    def __eq__(self, other):
    def __gt__(self, other):
    def __lt__(self, other):
    def __ge__(self, other):
    def __le__(self, other):
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __ge__(self, other):  # >= other is topik, because topik is right after >
        assert isinstance(other, (self.__class__, DogBig))
        return self.age >= other.age

    def __int__(self):
        return self.age

    def __repr__(self):
        return f'{self.__class__.__name__}: name={self.name}, age={self.age} '

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


badik = DogSmall('Badik', age=1)
topik = DogBig('Topik', age=2)

if badik >= topik:
    print("badik > topik")
else:
    print("badik < topik")

total_age = int(badik) + int(topik)  # add magic methods to have ability add two instances
print(total_age)

print(badik.__repr__())
