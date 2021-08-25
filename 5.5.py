from random import random

A = [int(random() * 10) for i in range(50)]

A.sort()

def remove(l):
    i = 0
    current = None
    while i < len(l):
        if current != None and l[i] == current:
            del l[i]
            continue
        i+=1
        current = l[i]