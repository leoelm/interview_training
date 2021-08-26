from ListNode import ListNode

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

def printList(l):
    while l:
        if not l.next:
            print(l.data)  
            break   
        print(l.data, '--> ', end='')
        l = l.next