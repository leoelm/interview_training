def string_to_int(s):
    out = 0
    for i, c in enumerate(reversed(s)):
        if c == '-':
            out *= -1
            continue
        out += 10**i * (ord(c) - 48)
    return out

def int_to_string(num):
    neg = False
    if num < 0:
        num *= -1
        neg = True
    upper_bound = 0
    while num > 10**upper_bound:
        upper_bound += 1

    out = ''
    for i in reversed(range(upper_bound)):
        val = num // 10**i
        num = num % 10**i

        out += chr(val + 48)

    return '-' + out if neg else out

print(int_to_string(-314))