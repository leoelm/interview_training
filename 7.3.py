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
# l1.next.next.next.next = l1.next

def detect(l):
    while l:
        try:
            if l.seen: return True
        except:
            l.seen = True
        l = l.next

    return False

print(detect(l1))