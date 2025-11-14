import heapq
class Node:
    def __init__(self, level, value, weight, bound, items):
        self.level = level
        self.value = value
        self.weight = weight
        self.bound = bound
        self.items = items
    def __lt__(self, other):
        return self.bound > other.bound
def bound(node, capacity, weights, values):
    if node.weight >= capacity:
        return 0
    profit_bound = node.value
    j = node.level + 1
    totweight = node.weight
    while j < len(weights) and totweight + weights[j] <= capacity:
        totweight += weights[j]
        profit_bound += values[j]
        j += 1
    if j < len(weights):
        profit_bound += (capacity - totweight) * values[j] / weights[j]
    return profit_bound
def knapsack_branch_and_bound(weights, values, capacity):
    n = len(weights)
    pq = []
    ratio = list(range(n))
    ratio.sort(key=lambda i: values[i]/weights[i], reverse=True)
    weights = [weights[i] for i in ratio]
    values  = [values[i] for i in ratio]
    root = Node(-1, 0, 0, 0, [])
    root.bound = bound(root, capacity, weights, values)
    heapq.heappush(pq, root)
    max_value = 0
    while pq:
        node = heapq.heappop(pq)
        if node.bound < max_value:
            continue
        next_level = node.level + 1
        if next_level >= n:
            continue
        w = node.weight + weights[next_level]
        v = node.value + values[next_level]
        if w <= capacity and v > max_value:
            max_value = v
        left = Node(next_level, v, w, 0, node.items + [ratio[next_level]])
        left.bound = bound(left, capacity, weights, values)
        if left.bound > max_value:
            heapq.heappush(pq, left)
        right = Node(next_level, node.value, node.weight, 0, node.items)
        right.bound = bound(right, capacity, weights, values)
        if right.bound > max_value:
            heapq.heappush(pq, right)
    return max_value
weights = [2, 3, 4, 5]
values  = [3, 4, 5, 6]
capacity = 5
print("Maximum Profit:", knapsack_branch_and_bound(weights, values, capacity))