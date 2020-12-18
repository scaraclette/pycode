class Node:
    def __init__(self, key):
        self.val = key
        self.right = None
        self.left = None

def iterativeInorder(root: Node):
    # Stack
    treeStack = []
    
    while root or treeStack != []:
        # Find left most node of the curr node
        while root:
            treeStack.append(root)
            root = root.left
        
        # Curr must be None at this point
        root = treeStack.pop()
        print(root.val)

        root = root.right

def iterativePreorder(root: Node):
    treeStack = [root]
    while treeStack != []:
        curr = treeStack.pop()
        print(curr.val)
        if curr.right:
            treeStack.append(curr.right)
        if curr.left:
            treeStack.append(curr.left)

def iterativePostorder(root: Node):
    treeStack = []
    while root:
        if root.right:
            treeStack.append(root.right)
        treeStack.append(root)



def main():
    root = Node(1) 
    root.left = Node(2) 
    root.right = Node(3) 
    root.left.left = Node(4) 
    root.left.right = Node(5) 
    # iterativeInorder(root)
    iterativePreorder(root)

main()