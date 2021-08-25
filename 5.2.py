def increment(l):
    carry = False
    for i in reversed(range(len(l))):
        if not carry and i != len(l) - 1:
            break
        carry = False
        l[i] = (l[i] + 1) % 10

        if l[i] == 0:
            carry = True 

        if carry and i == 0:
            l[0] = 1
            l.append(0)

    return l
A = [9,9,9]

print(increment(A))