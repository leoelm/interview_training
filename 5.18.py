A = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

B = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def spiral(A):
    out = []

    while len(A) != 0:
        try:
            out = out + A[0]
            del A[0]
        except:
            continue

        try:
            out = out + [i.pop() for i in A]
        except:
            continue

        try:
            out = out + A[-1][::-1]
            del A[-1]
        except:
            continue
        
        try:
            out = out + [i.pop(0) for i in A][::-1]
        except:
            continue

    return out

print(spiral(B))

      