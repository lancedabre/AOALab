import heapq
def tsp_branch_and_bound(graph):
    n = len(graph)
    pq = []
    def calculate_bound(path, cost):
        remaining = set(range(n)) - set(path)
        b = cost
        for r in remaining:
            b += min(graph[r])   # optimistic
        return b
    start = [0]
    bound = calculate_bound(start, 0)
    heapq.heappush(pq, (bound, 0, 1, start))
    best_cost = float('inf')
    best_path = None
    while pq:
        bd, cost, level, path = heapq.heappop(pq)
        if bd > best_cost:
            continue
        if level == n:
            final_cost = cost + graph[path[-1]][path[0]]
            if final_cost < best_cost:
                best_cost = final_cost
                best_path = path + [0]
            continue
        for nxt in range(n):
            if nxt not in path:
                new_cost = cost + graph[path[-1]][nxt]
                new_path = path + [nxt]
                new_bound = calculate_bound(new_path, new_cost)
                if new_bound < best_cost:
                    heapq.heappush(pq, (new_bound, new_cost, level+1, new_path))
    return best_cost, best_path
graph = [
    [0, 20, 30, 10],
    [15, 0, 16, 4],
    [3,  5, 0,  2],
    [19, 6, 18, 0]
]
best_cost, best_path = tsp_branch_and_bound(graph)
print("Best Cost:", best_cost)
print("Best Path:", best_path)