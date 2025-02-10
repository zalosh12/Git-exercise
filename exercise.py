from collections import  deque
class Queue:
    def __init__(self):
        self.arr = []

    def append(self,item):
        self.arr.append(item)

    def pop(self):
        if not self.arr:
            return -1
        return self.arr.pop(0)

    def peek(self):
        if self.arr:
            return self.arr[0]
        return -1

m = Queue()
m.append(9)
m.pop()
m.append(8)
m.append(7)
m.append(7)

saved = m.peek()

z = Queue()

save = m.peek()

while True:
    saved = m.peek()
    m.append(m.pop())
    save1 = m.peek()
    if m.peek() == saved:
        break

    z.append(saved - save1)

# k = "ljj"
# print(isinstance(k,int))

lk = [4,9,0]
print(all(x % 2 == 0 for x in lk))
m = [[2,3,1], [0], [0,4], [0], [2]]


def bfsOfGraph(adj):
    res = []
    visited = set()
    q = deque([0])
    while q:
        cur = q.popleft()
        for i in adj[cur]:
            if i not in visited:
                q.append(i)
        res.append(cur)
        visited.add(cur)
    return res
print(bfsOfGraph(m))




