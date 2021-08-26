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

def reverse(l, s, f):
    temp = []
    count = 1

    head = n = l

    end, start = None, None

    while count <= f:
        if count == s-1:
            start = n
        if count >= s:
            temp.append(n)
        count += 1
        n = n.next

    end = n

    for i in reversed(range(len(temp))):
        node = temp[i]
        if len(temp) - 1 == i:
            start.next = node
        if i == 0:
            node.next = end
            break
        node.next = temp[i-1]

    return start

h = reverse(l1, 2, 3)
printList(h)