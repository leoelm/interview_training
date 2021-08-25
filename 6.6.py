s = "Alice likes Bob lots"

def reverse(s):
    temp = s.split()

    l, r = 0, len(temp) - 1

    while l < r:
        temp[l], temp[r] = temp[r], temp[l]
        l += 1
        r -= 1

    return ' '.join(temp)

print(reverse(s))