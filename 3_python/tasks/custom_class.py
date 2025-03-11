class CustomClass:
    __slots__ = ("course", "price")

    def __init__(self):
        self.course = "DSA Self Paced"
        self.price = 3999


custom = CustomClass()

print(custom.course)
print(custom.price)
