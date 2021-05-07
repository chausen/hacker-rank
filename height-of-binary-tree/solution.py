class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None
        self.level = 0

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
            self.root.level = 0
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        current.left.level = current.level + 1
                        if current.left.level > self.level:
                            self.level = current.left.level
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        current.right.level = current.level + 1
                        if current.right.level > self.level:
                            self.level = current.right.level                        
                        break
                else:
                    break


# not using the level on the node objects                
def height_recursive(root):    
    def find_height(node, level):
        l, r = level, level
        if node.left:
            l = find_height(node.left, level + 1)
        if node.right:
            r = find_height(node.right, level + 1)
        return max(l, r)

    return find_height(root, 0)

def height_recursive_better(root):
    l, r = 0, 0
    if root.left:
        l = 1 + height_recursive_better(root.left)
    if root.right:
        r = 1 + height_recursive_better(root.right)

    return max(l, r)

def height(root):
    return root.level

def print_tree(root):
    if root.left:
        print_tree(root.left)
    print(f'{root.info}, level: {root.level}')
    if root.right:
        print_tree(root.right)

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

print(height_recursive_better(tree.root))
# print_tree(tree.root)
