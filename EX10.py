from collections import deque
class Graph:

    def __init__(self):
        self.graph = {}
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def display(self):
        print("Graph Representation")
        for vertex in self.graph:
            print(vertex, "->", self.graph[vertex])

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)
        print("BFS Traversal:", end=" ")
        while queue:
            vertex = queue.popleft()
            print(vertex, end=" ")
            for neighbour in self.graph[vertex]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
        print()

    def dfs(self, start):
        visited = set()
        print("DFS Traversal:", end=" ")
        self.dfs_recursive(start, visited)
        print()

    def dfs_recursive(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=" ")
        for neighbour in self.graph[vertex]:
            if neighbour not in visited:
                self.dfs_recursive(neighbour, visited)

g = Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_vertex("E")

g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.add_edge("B", "E")
g.add_edge("C", "E")
g.display()
g.bfs("A")
g.dfs("A")