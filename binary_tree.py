from node import Node

class BinaryTree:
    def __init__(self, head: Node):
        self.head = head

    def add(self, *args):
        for new_node in args:
            current_node = self.head
            while current_node:
                if current_node.value == new_node.value:
                    raise ValueError('Value already in binary tree')
                elif new_node.value > current_node.value:
                    if current_node.right:
                        current_node = current_node.right
                    else:
                        current_node.right = new_node
                        break
                else:
                    if current_node.left:
                        current_node = current_node.left
                    else:
                        current_node.left = new_node
                        break

    def inorder(self):
        print('INORDER')
        self._inorder_recursive(self.head)

    def _inorder_recursive(self, current_node):
        if not current_node: # checks current node isn't None
            print(f'Path ended\n')
            return

        print(f'{current_node.value} moving left')
        self._inorder_recursive(current_node.left)
        print(f'Current Node: {current_node.value}')
        print(f'{current_node.value} moving right')
        self._inorder_recursive(current_node.right)

    def preorder(self):
        print('PREORDER')
        self._preorder_recursive(self.head)

    def _preorder_recursive(self, current_node):
        if not current_node:
            print('Path ended\n')
            return
        print(f'Current Node: {current_node.value}')
        print(f'{current_node.value} moving left')
        self._preorder_recursive(current_node.left)
        print(f'{current_node.value} moving right')
        self._preorder_recursive(current_node.right)

    def find(self, value):
        current_node = self.head
        while current_node:
            if value == current_node.value:
                return current_node
            elif value > current_node.value:
                current_node = current_node.right
            else:
                current_node = current_node.left
        raise LookupError('Couldn\'t find your value')


"""
Following trees formation:

                        100
                     /       \
                   99       101
                   /           \
                84              105
                  \
                   94


In-order traversal
"""
inorder_tree = BinaryTree(Node(100)) # make head of tree
inorder_tree.add(Node(99), Node(101), Node(84), Node(105), Node(94)) # add these nodes with the add algorithm
inorder_tree.inorder() # traverses through the tree using in-order algorithm. Go as far left, print node, and then go right on each node and print


"""
Preorder traversal
"""
preorder_tree = BinaryTree(Node(100))
preorder_tree.add(Node(99), Node(101), Node(84), Node(105), Node(94))
preorder_tree.preorder() # traverses through tree with preorder algorithm. Print the current node, then go left as far as you can, then go right for each node

"""
Finding
"""
find_tree = BinaryTree(Node(100))
find_tree.add(Node(99), Node(101), Node(84), Node(105), Node(94))
print(find_tree.find(84))
