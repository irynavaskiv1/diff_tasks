# The zip() function takes iterables (can be zero or more), aggregates them in a tuple, and return it.
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")

x = zip(a, b)
print(list(x))  # [('John', 'Jenny'), ('Charles', 'Christy'), ('Mike', 'Monica')]
