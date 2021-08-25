def base_conversion(num, base):
    neg = False
    if num < 0:
        neg, num = True, -num
    upper = 0
    while num > base ** upper:
        upper += 1

    out = ''
    for i in reversed(range(upper)):
        val = num // base ** i
        num = num % base ** i

        out += str(val)

    return "-" + out if neg else out

print(base_conversion(-80, 8))