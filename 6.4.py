from random import choice

A = [choice(['a', 'b', 'c', 'd']) for i in range(10)]

#O(n) time, O(n) space
def swap(l):
    out = []
    for i, c in enumerate(l):
        if c == 'a':
            out += ['d', 'd']
        elif c == 'b':
            continue
        else:
            out.append(c)

    return out