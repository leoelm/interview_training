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
l2.next = l1
l2.next.next = ListNode(13)

def overlap(l1, l2):
    while l1:
        l1.seen = True
        l1 = l1.next
    while l2:
        try:
            if l2.seen:
                return True
        except:
            l2 = l2.next

    return False

print(overlap(l1, l2))