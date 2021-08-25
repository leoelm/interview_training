from random import random, choice
import copy

A = [int(random() * 50) for i in range(50)]

def subset(l, num):
    indices = [False] * len(l)
    out = []
    while len(out) != num:
        index = choice(range(len(l)))
        if not indices[index]:
            out.append(l[index])
            indices[index] = False

    return out

print(subset(A, 10))