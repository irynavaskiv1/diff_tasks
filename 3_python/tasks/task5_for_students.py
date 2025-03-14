# Swap values for x and y with one line
# Input
x = 3
y = 4
print(f"x {x} y {y}")

x, y = y, x
print(f"x {x} y {y}")

# Compare x and y, select the minimum value and
# print it using the ternary operator
x = 3
y = 4
num = y if y < x else x
print(f"Minimum value is {num}")

# Leave only even numbers in the list and square them
numbers = [1, 2, 3, 4, 5, 6]
upd_num = [x * 2 for x in numbers]
print(upd_num)

# Calculate the sum of the numbers from 1 to 1000 using lambda
from functools import reduce

total = reduce(lambda x, y: x + y, range(1, 1001))
print(total)

# Display the names of the animals in order from youngest to oldest

animals = [
    {"type": "penguin", "name": "Stephanie", "age": 8},
    {"type": "elephant", "name": "Devon", "age": 3},
    {"type": "puma", "name": "Moe", "age": 5},
]
sorted = sorted(animals, key=lambda animal: animal["age"])
print([animal["name"] for animal in animals])

# Write a Python program to get the Python version you are using
import sys

print(sys.version)
