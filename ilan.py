class Que:
    def __init__(self):
        self.arr = []
        self.size = 0

    def enqueue(self,val):
        self.arr.append(val)
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return "The queue is empty"
        self.size -= 1
        return self.arr.pop(0)

    def front(self):
        if self.size == 0:
            return "The queue is empty"
        return self.arr[0]

    def is_empty(self):
        return self.size == 0

my = Que()
