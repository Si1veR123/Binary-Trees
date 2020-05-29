class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f'<Node {self.value}>'
# node is a value with a left and right value to resemble a tree
