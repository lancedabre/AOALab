def floyd_warshall(graph):
    n = len(graph)
    dist = [row[:] for row in graph]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist
INF = float('inf')
graph = [
    [0,   3, INF, 5],
    [2,   0, INF, 4],
    [INF, 1, 0,   INF],
    [INF, INF, 2, 0]
]

print("All-Pairs Shortest Paths:")
result = floyd_warshall(graph)
for row in result:
    print(row)