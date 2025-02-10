class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head

    def add(self,val):
        new_node = Node(val)
        if self.head is None:
            self.head = self.tail = new_node
        self.tail.next = new_node
        self.tail = self.tail.next

    def pop(self):
        if self.head:
            prev = self.head.val
            self.head = self.head.next
            return prev

    def print_lst(self):
        current = self.head
        while current:
            print(current.val)
            current = current.next

    def rec_print(self):
        def rec(current):
          if current is None:
              return
          print(current.val)
          rec(current.next)
        rec(self.head)


if __name__ ==  "__main__":
    l = LinkedList()
    l.add(9)
    l.add(20)
    l.add(7)
    l.add(9)
    l.add(6)
    l.add(8)
    # l.print_lst()
    l.rec_print()


