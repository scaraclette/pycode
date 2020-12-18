# Python program to print tree traversals
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Inorder
def printInorder(root: Node):
    if root:
        printInorder(root.left)
        print(root.val, end=" ")
        printInorder(root.right)

# Preorder
def printPreOrder(root: Node):
    if root:
        print(root.val, end=" ")
        printPreOrder(root.left)
        printPreOrder(root.right)

# Postorder
def printPostOrder(root: Node):
    if root:
        printPostOrder(root.left)
        printPostOrder(root.right)
        print(root.val, end=" ")

def driver():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    printPreOrder(root)
    print()
    printPostOrder(root)
    print()
    printInorder(root)
    print()

driver()