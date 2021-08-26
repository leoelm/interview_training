from BinaryTree import BinaryTree, inorder

t = BinaryTree(val = 1)
t.left = BinaryTree(val = 2)
t.right = BinaryTree(val = 3)
t.left.left = BinaryTree(val = 4)
t.left.right = BinaryTree(val = 5)
t.right.left = BinaryTree(val = 6)
t.right.right = BinaryTree(val = 7)

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