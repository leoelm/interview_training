class BinaryTree():
    def __init__(self, val = None, right = None, left = None, parent = None):
        self.val = val
        self.right = right
        self.left = left
        self.parent = parent

def inorder(n):
    if not n:
        return 
    inorder(n.left)
    print(n.val)
    inorder(n.right)

def preorder(n):
    if not n:
        return 
    print(n.val, end='')
    preorder(n.left)
    preorder(n.right)

def postorder(n):
    if not n:
        return
    postorder(n.left)
    postorder(n.right)
    print(n.val, end='')