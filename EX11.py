import heapq

def dijkstra(graph, source):
# Initialize distances
    distance = {vertex: float('inf') for vertex in graph}
    distance[source] = 0
# Priority queue: (distance, vertex)
    pq = [(0, source)]
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
# Ignore outdated entries
        if current_distance > distance[current_vertex]:
            continue
# Check all adjacent vertices
        for neighbor, weight in graph[current_vertex]:
            new_distance = current_distance + weight
            if new_distance < distance[neighbor]:
                distance[neighbor] = new_distance
                heapq.heappush(pq, (new_distance, neighbor))
    return distance
# Weighted graph
graph = {
'A': [('B', 4), ('C', 1)],
'B': [('D', 1)],
'C': [('B', 2), ('D', 5)],
'D': [('E', 3)],
'E': []
}
source = 'A'
shortest_distances = dijkstra(graph, source)

print("Shortest distances from source vertex", source)
for vertex, dist in shortest_distances.items():
    print(source, "->", vertex, "=", dist)