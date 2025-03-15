class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert_class(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.insert_class(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.insert_class(data)
        else:
            self.data = data

    def find(self, value):
        if value < self.data:
            if self.left is None:
                return str(value) + " not found"
            return self.left.find(value)  # recursion
        elif value > self.data:
            if self.right is None:
                return str(value) + " not found"
        else:
            return str(value) + " is found"

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()
        print(self.data)


node = Node(12)
node.insert_class(7)
node.insert_class(17)
node.print_tree()
print(node.find(5))
