from ListNode import ListNode, printList

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