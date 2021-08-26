class BinaryTree():
    def __init__(self, val = None, right = None, left = None, parent = None):
        self.val = val
        self.right = right
        self.left = left
        self.parent = parent


t = BinaryTree(val = 1)
t.left = BinaryTree(val = 2, parent = t)
t.right = BinaryTree(val = 2, parent = t)
t.left.right = BinaryTree(val = 3, parent=t.left)
t.left.right.right = BinaryTree(val = 4, parent=t.left)
t.right.left = BinaryTree(val = 3, parent=t.right)
t.right.left.left = BinaryTree(val = 4, parent=t.right)

global out
out = ''
def symmetric(t):
    def helper(t):
        global out
        if not t:
            return ''
        helper(t.left)
        out += str(t.val)
        helper(t.right)

        return out

    o = helper(t)
    l = o[:(len(o) // 2)]
    r = o[(len(o) // 2) + 1:]

    return l == r[::-1]

print(symmetric(t))