class Node():
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

def inorder(root):
    if root is None:
        return None
    inorder(root.left)
    print(root.value)
    inorder(root.right)

def CloneBST(root):
    if root is None:
        return None
    root_copy = Node(root.value)
    # clone left subtree
    root_copy.left = CloneBST(root.left)
    root_copy.right = CloneBST(root.right)
    return root_copy

if __name__=="__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.right = Node(5)

    clone = CloneBST(root)
    inorder(clone)
