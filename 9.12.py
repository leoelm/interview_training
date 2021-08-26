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
    print(n.val, end=' ')
    inorder(n.right)

def preorder(n):
    if not n:
        return 
    print(n.val, end=' ')
    preorder(n.left)
    preorder(n.right)


A = ['F', 'B', 'A', 'E', 'H', 'C', 'D', 'I', 'G']
B = ['H', 'B', 'F', 'E', 'A', 'C', 'D', 'G', 'I']

def construct(inorder, preorder):
    if len(preorder) == 0:
        return 
    root = BinaryTree(val = preorder[0])

    inorder_right = inorder[inorder.index(root.val)+1:]
    preorder_right = []
    if len(inorder_right) != 0: preorder_right = preorder[-len(inorder_right):]

    inorder_left = inorder[:inorder.index(root.val)]
    preorder_left = preorder[1:len(inorder_left)+1]

    root.right = construct(inorder_right, preorder_right)
    root.left = construct(inorder_left, preorder_left)

    return root

t = construct(A, B)

inorder(t)
print()
preorder(t)
