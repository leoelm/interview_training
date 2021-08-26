from BinaryTree import BinaryTree

tree = BinaryTree(val=10)
tree.left = BinaryTree(val=5)
tree.right = BinaryTree(val=8)
tree.left.left = BinaryTree(val=3)
tree.left.right = BinaryTree(val=6)
tree.left.right.left = BinaryTree(val=7)
tree.left.right.right = BinaryTree(val=9)
tree.right.left = BinaryTree(val=13)
tree.right.right = BinaryTree(val=17)

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