class BinaryTree():
    def __init__(self, val = None, right = None, left = None, parent = None):
        self.val = val
        self.right = right
        self.left = left
        self.parent = parent


t = BinaryTree(val = 1)
t.left = BinaryTree(val = 2, parent = t)
t.right = BinaryTree(val = 3, parent = t)
t.left.left = BinaryTree(val = 4, parent = t.left)
t.left.right = BinaryTree(val = 5, parent=t.left)
t.right.left = BinaryTree(val = 6, parent=t.right)
t.right.right = BinaryTree(val = 7, parent=t.right)

#O(h) time, O(h) space
def lca(left, right):
    left_parents = [left.parent]
    pleft = left.parent
    while pleft:
        if pleft.parent == None:
            break
        left_parents.append(pleft.parent)
        pleft = pleft.parent

    pright = right
    while pright:
        if pright.parent in left_parents:
            return pright.parent
        pright = pright.parent

def depth(n):
    if not n.parent:
        return 0
    
    return depth(n.parent) + 1

def lca2(left, right):
    dleft = depth(left)
    dright = depth(right)

    diff = abs(dleft - dright)

    if dright > dleft:
        left, right = right, left

    while diff:
        left = left.parent
        diff -= 1
    while left != right:
        left, right = left.parent, right.parent

    return left

print(lca2(t.left, t.right.left).val)