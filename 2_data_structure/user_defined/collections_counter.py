# 1) counter implementation

from collections import Counter

# With sequence of items / count items in list
print(Counter(['B', 'B', 'A', 'B', 'C', 'A', 'B', 'B', 'A', 'C']))
print(Counter(['3', 'i', '3', '5', 55, '8', 'ira', 'hello']))

# with dictionary / sort dict values
print(Counter({'A': 3, 'B': 5, 'C': 2}))
print(Counter({'A': 3, 'B': 5, 'C': 2, '33': 'ira'}))

# with keyword arguments
print(Counter(A=3, B=5, C=2))
