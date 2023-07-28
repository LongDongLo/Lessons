## binary tree in python
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# A function to do inorder tree traversal
def printInorder(root):
    if root:
        # First recur on left child
        printInorder(root.left)

        # then print the data of node
        print(root.val),

        # now recur on right child
        printInorder(root.right)

# A function to do inorder tree traversal
def printPreorder(root):
    if root:
        # then print the data of node
        print(root.val),

        # First recur on left child
        printPreorder(root.left)

        # now recur on right child
        printPreorder(root.right)

# A function to do inorder tree traversal
def printPostorder(root):
    if root:

        # First recur on left child
        printPostorder(root.left)

        # now recur on right child
        printPostorder(root.right)

        # then print the data of node
        print(root.val),

def

# Driver code
if __name__ == "__main__":
    root = Node(0)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    # Function call
    print("\nPreorder traversal of binary tree is")
    printPreorder(root)
