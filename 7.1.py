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

l1 = ListNode(2)
l1.next = ListNode(5)
l1.next.next = ListNode(7)

l2 = ListNode(3)
l2.next = ListNode(11)
l2.next.next = ListNode(13)

def merge(l1, l2):
    head = out = ListNode()

    while l1 and l2:
        if l1.data < l2.data:
            l1, out.next = l1.next, l1
        else:
            l2, out.next = l2.next, l2

        out = out.next

    out.next = l1 or l2

    return head.next

merged = merge(l1, l2)

printList(merged)