class BinaryTree():
    def __init__(self, val = None, right = None, left = None):
        self.val = val
        self.right = right
        self.left = left


t = BinaryTree(val = 1)
t.left = BinaryTree(val = 2)
t.right = BinaryTree(val = 3)
t.left.left = BinaryTree(val = 4)
t.left.right = BinaryTree(val = 5)
t.right.left = BinaryTree(val = 6)
t.right.right = BinaryTree(val = 7)

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

def height(n):
    if not n:
        return 0
    
    return max(height(n.left), height(n.right)) + 1

def balanced(n):
    if not n:
        return True

    lh = height(n.left)
    rh = height(n.right)

    return abs(lh - rh) <= 1 and balanced(n.left) and balanced(n.right)

print(inorder(t))