from after import LinkedList


class Queue:
    def __init__(self):
        self.__arr = LinkedList()
        self.__size = 0

    def enqueue(self,item):
        self.__arr.add(item)
        self.__size += 1

    def dequeue(self):
        if self.is_empty():
            return
        self.__size -= 1
        return self.__arr.pop()

    def is_empty(self):
        return not self.__size

    def peek(self):
        if not self.is_empty():
           return self.__arr.head.val

    def clear(self):
        self.__init__()


my_q = Queue()
my_q.enqueue(8)
my_q.enqueue(6)
my_q.enqueue(9)
print(my_q.dequeue())


