# Program 12: Implementation of Minimum Spanning Tree Algorithms
# Kruskal's and Prim's Algorithms
class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
        elif self.rank[ra] > self.rank[rb]:
            self.parent[rb] = ra
        else:
            self.parent[rb] = ra
            self.rank[ra] += 1
        return True

def kruskal(n, edges):
    edges = sorted(edges, key=lambda x: x[2])
    ds = DisjointSet(n)
    mst = []
    total = 0
    for u, v, w in edges:
        if ds.union(u, v):
            mst.append((u, v, w))
            total += w
            if len(mst) == n - 1:
                break
    return mst, total

def prim(n, graph):
    selected = [False] * n
    selected[0] = True
    mst = []
    total = 0

    for _ in range(n - 1):
        min_edge = None
        for u in range(n):
            if selected[u]:
                for v, w in graph[u]:
                    if not selected[v]:
                        if min_edge is None or w < min_edge[2]:
                            min_edge = (u, v, w)
        if min_edge is None:
            break

        u, v, w = min_edge
        selected[v] = True
        mst.append((u, v, w))
        total += w

    return mst, total

# Vertices: 0, 1, 2, 3, 4
edges = [
(0, 1, 2),
(0, 3, 6),
(1, 2, 3),
(1, 3, 8),
(1, 4, 5),
(2, 4, 7),
(3, 4, 9)
]
graph = [[] for _ in range(5)]
for u, v, w in edges:
    graph[u].append((v, w))
    graph[v].append((u, w))
kruskal_mst, kruskal_cost = kruskal(5, edges)
prim_mst, prim_cost = prim(5, graph)
print("Kruskal's Algorithm")
for u, v, w in kruskal_mst:
    print(f"{u} - {v} : {w}")
print("Minimum Cost:", kruskal_cost)

print("\nPrim's Algorithm")
for u, v, w in prim_mst:
    print(f"{u} - {v} : {w}")
print("Minimum Cost:", prim_cost)