class ListNode:
    def __init__(self, data=0, next_node = None):
        self.data = data
        self.next_node = next_node

def search(node, value):
    if node.data == value:
        return True
    while node.next_node:
        node = node.next_node
        if node.data == value:
            return True

    return False

def insert(node, value):
    new = ListNode(data = value)

    new.next_node = node.next_node
    node.next_node = new

def delete(node):
    node.next = node.next.next