stack = []

A = '3,4,+,2,x,1,+'
B = "3,4,+"

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def evaluate(exp):
    temp = exp.split(',')

    stack.append(int(temp[0]))
    del temp[0]

    while len(temp) != 0:

        val = temp[0]

        if RepresentsInt(val):
            stack.append(int(val))
            del temp[0]
        else:

            operations = {'+': lambda x, y: x+y, '-': lambda x, y: x-y, '/': lambda x, y: x/y, 'x': lambda x, y: x*y}

            o2 = stack.pop()
            o1 = stack.pop()
            
            stack.append(operations[val](o1, o2))

            del temp[0]

    return stack.pop()

print(evaluate(A))