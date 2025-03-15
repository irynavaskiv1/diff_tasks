# A stack is a linear data structure that stores items in a LIFO or FILO manner.

stack = []
stack.append("a")
stack.append("b")
stack.append("c")

print("Initial stack")
print(stack)

print("\nElements popped from stack:")
print(stack.pop())
print(stack.pop())
print(stack.pop())

print("\nStack after elements are popped:")
print(stack)
