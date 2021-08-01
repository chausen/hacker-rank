class Node:
    left = None
    right = None

    def __init__(self, val):
        self.value = val

def in_order(node):
    if (node):
        in_order(node.left)
        print(node.value)
        in_order(node.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
in_order(root)

