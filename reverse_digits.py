#should be O(n) where n is the number of digits
def reverse_digits(num):
    return int(str(num)[::-1])

#O(n)
def reverse_digits_2(num):
    result, remainder = 0, abs(num)
    while remainder:
        result = result * 10 + remainder % 10
        remainder = remainder // 10

    return -result if num < 0 else result 
    