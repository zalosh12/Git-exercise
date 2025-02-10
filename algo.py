from  collections import deque
class Graph(object):
    def __init__(self,vertices):
        self.graph = {}
        for i in range(vertices):
            self.graph[i] = []

    def add_neighbour(self, source, dest):
        self.graph[source].append(dest)

    def visualize(self):
        for src, neighbors in self.graph.items():
            print(f"{src} -> {neighbors}")

    def bfs(self,s):
        visited = [False] * len(self.graph)
        q = deque([s])
        visited[s] = True

        while q:
            cur = q.popleft()
            print(cur, end= " ")
            for neighbor in self.graph[cur]:
                if not visited[neighbor]:
                    q.append(neighbor)
                    visited[neighbor] = True


def main():
    g = Graph(4)
    g.add_neighbour(0, 1)
    g.add_neighbour(0, 2)
    # g.add_neighbour(1, 0)
    g.add_neighbour(1, 2)
    # g.add_neighbour(1, 3)
    g.add_neighbour(2, 0)
    g.add_neighbour(2, 3)
    # g.add_neighbour(2, 1)
    # g.add_neighbour(3, 1)

    g.bfs(2)
    print()





    g.visualize()
if __name__ == "__main__":
     main()
