class BinaryNode():
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

tree = BinaryNode(10)
tree.left = BinaryNode(5)
tree.right = BinaryNode(8)
tree.left.left = BinaryNode(3)
tree.left.right = BinaryNode(6)
tree.left.right.left = BinaryNode(7)
tree.left.right.right = BinaryNode(9)
# tree.right = BinaryNode(15)
tree.right.left = BinaryNode(13)
tree.right.right = BinaryNode(17)

#o(n), I believe
def dfs(t):
    q = []

    q.append(t)
    while q:
        count = len(q)
        for i, val in enumerate(q):
            print(val.value, end=' ')

        for i in range(count):
            if q[0].left: q.append(q[0].left)
            if q[0].right: q.append(q[0].right)

            del q[0]
        print()

dfs(tree)