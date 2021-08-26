from BinaryTree import BinaryTree

t = BinaryTree(val = 1)
t.left = BinaryTree(val = 2, parent = t)
t.right = BinaryTree(val = 2, parent = t)
t.left.right = BinaryTree(val = 3, parent=t.left)
t.left.left = BinaryTree(val = 4, parent=t.left)
t.right.left = BinaryTree(val = 3, parent=t.right)
t.right.right = BinaryTree(val = 4, parent=t.right)

def inorder(t):
    prev, result = None, []

    while t:
        next = None
        if prev == t.parent:
            if t.left:
                next = t.left
            else:
                result.append(t.val)

                next = t.right or t.parent

        elif t.left is prev:
            result.append(t.val)

            next = t.right or t.parent
        
        else:
            next = t.parent

        prev, t = t, next

    return result

print(inorder(t))
