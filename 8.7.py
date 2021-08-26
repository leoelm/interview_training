class CircularQueue():
    def __init__(self, size):
        self.queue = [None] * size
        self.size = size
        self.first = size // 2
        self.last = size // 2 + 1

    def prepend(self, item):
        if self.first == -1:
            self.queue = [None] * 10 + self.queue
            self.first = 9
            self.size += 10

        self.queue[self.first] = item
        self.first -= 1

    def append(self, item):
        self.queue[self.last] = item
        self.last += 1

    def size(self):
        return self.size

    def dequeu(self):
        return self.queue[self.first]
    