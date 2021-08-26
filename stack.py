class Stack():
    def __init__(self):
        stack = []

    def pop(self):
        item = self.stack[-1]
        del self.stack[-1]
        return item

    def push(self, item):
        self.stack.append(item)

    #O(n) time, O(1) space
    def max(self):
        m = None
        for i in self.stack:
            if m == None:
                m = i
            elif m < i:
                m = i

        return m
