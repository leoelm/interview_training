#O(n) where n is the number of bits
def parity(num):
    result = 0
    while num:
        result ^= (num & 1) #get least significant bit of num and then XOR with result
        num >>= 1 #shift num by one bit to the right

    return result

#0(k) where k is the number of set bits
def parity2(num):
    result = 0
    while num: #does until num == 0 i.e. all set bits are erased
        result ^= 1
        num &= (num - 1) #erases the lowest set bit
    return result