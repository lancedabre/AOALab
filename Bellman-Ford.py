def bellman_ford(vertices, edges, source):
    dist = [float('inf')] * vertices
    dist[source] = 0
    for _ in range(vertices - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            print("Graph contains a negative weight cycle")
            return None

    return dist
V = 5
edges = [
    (0, 1, -1),
    (0, 2, 4),
    (1, 2, 3),
    (1, 3, 2),
    (1, 4, 2),
    (3, 2, 5),
    (3, 1, 1),
    (4, 3, -3)
]
distances = bellman_ford(V, edges, 0)
print("Shortest Distances:", distances)