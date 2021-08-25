import re

s = "A man,a plan, a canal Panama."

#O(n) time, O(1) space
def palindrom(s):
    s = re.sub('[\W_]', '', s).lower()
    
    l, r = 0, len(s) - 1

    while s[l] == s[r] and l < r:
        l += 1
        r -= 1

    return (r - l == -1 and len(s) % 2 == 0) or (r - l == 0)


print(palindrom(s))