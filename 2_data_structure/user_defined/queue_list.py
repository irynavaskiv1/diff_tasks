# Queue is a linear data structure that stores items in First In First Out (FIFO) manner.

queue = []
queue.append('a')
queue.append('b')
queue.append('c')

print("Initial queue")
print(queue)

print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print("\nQueue after removing elements")
print(queue)
