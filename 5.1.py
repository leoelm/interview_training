from random import random, choice

A = [random() for i in range(10)]

def quicksort(l):
    if len(l) <= 1:
        return l
    pivot = choice(l)
    left = [i for i in l if i <= pivot]
    right = [i for i in l if i > pivot]
    
    return quicksort(left) + quicksort(right)