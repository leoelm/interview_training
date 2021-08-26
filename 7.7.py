class ListNode:
    def __init__(self, data=0, next_node = None):
        self.data = data
        self.next = next_node

def printList(l):
    while l:
        if not l.next:
            print(l.data)  
            break   
        print(l.data, '--> ', end='')
        l = l.next

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)

def delete(l, k):
    n1 = l
    n2 = l

    count = 0
    while n1:
        if count == k + 1:
            n2 = n2.next
        else:
            count += 1

        n1 = n1.next

    if n2 == l and count != k + 1:
        return n2.next

    n2.next = n2.next.next

    return l
    
node = delete(l1, 3)

printList(node)