class Que:
    def __init__(self,capacity):
        self.__arr = [None] * capacity
        self.__size = 0
        self.__head = 0
        self.__tail = 0

    def append(self,item):
        if self.is_full():
            print("the que is full")
            return
        self.__arr[self.__tail] = item
        self.__tail = (self.__tail + 1) % len(self.__arr)
        self.__size += 1


    def is_full(self):
        return self.__size == len(self.__arr)

    def is_empty(self):
        return self.__size == 0
        print("bye")


    def pop(self):
        if self.is_empty():
            print("the que is empty")
            return
        value = self.__arr[self.__head]
        self.__head = (self.__head + 1) % (len(self.__arr))
        self.__size -= 1
        return value

    def peek(self):
        return self.__arr[self.__head]



if __name__ == "__main__":
    my = Que(6)
    my.append(5)
    my.append(9)
    my.pop()
    print(my.peek())

