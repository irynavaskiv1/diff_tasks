class ItersIra:
    def __init__(self, value):
        self.data = value

    def __getitem__(self, item):
        return self.data[item]

    def __iter__(self):
        self.x = 0
        return self

    def __next__(self):
        if self.x == len(self.data):
            raise StopIteration
        item = self.data[self.x]
        self.x += 1
        return item

    def __contains__(self, x):
        return x in self.data


X = ItersIra([1, 2, 3, 4, 5])
print(3 in X)
