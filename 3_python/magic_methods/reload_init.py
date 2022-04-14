class Number:
    def __init__(self, start):
        self.data = start

    def sub(self, other):
        return Number(self.data - other)


X = Number(5)
print(X.data)

Y = X.data
Y = Y - 2
print(Y)
