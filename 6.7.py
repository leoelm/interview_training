MAPPING = ('0', '1', 'ABC', 'DEF', 'GHI', 'lKL', 'llNO', 'PQRS', 'TUV', 'IJXYZ')

def phone(number):
    def phone_helper(digit):
        if digit == len(number):
            mnemonics.append(''.join(partial))

        else:
            for c in MAPPING[int(number[digit])]:
                partial[digit] = c
                phone_helper(digit + 1)

    mnemonics, partial = [], [0] * len(number)
    phone_helper(0)
    return mnemonics

print(phone('234'))