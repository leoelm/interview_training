#O(2^n) where n is the number of bits of y
def x_pow_y(x, y):
    result = x
    while y - 1 != 0:
        result *= x
        y -= 1

    return result

#O(n) where n is the number of bits of y
def x_pow_y_2(x, y):
    result, power = 1.0, y

    while power:
        if power & 1:
            result *= x
        x, power = x * x, power >> 1

    return result

print(x_pow_y_2(1.7, 5))
print(pow(1.7, 5))