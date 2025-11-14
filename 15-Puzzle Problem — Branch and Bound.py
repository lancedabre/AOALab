import heapq
def manhattan(puzzle, goal):
    dist = 0
    for i in range(4):
        for j in range(4):
            val = puzzle[i][j]
            if val != 0:
                goal_i = (val - 1) // 4
                goal_j = (val - 1) % 4
                dist += abs(i - goal_i) + abs(j - goal_j)
    return dist
def get_neighbors(puzzle):
    neighbors = []
    # Find zero tile
    for i in range(4):
        for j in range(4):
            if puzzle[i][j] == 0:
                x, y = i, j
                break
    moves = [(0,1),(0,-1),(1,0),(-1,0)]
    for dx,dy in moves:
        nx, ny = x+dx, y+dy
        if 0 <= nx < 4 and 0 <= ny < 4:
            new_board = [row[:] for row in puzzle]
            new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]
            neighbors.append(new_board)
    return neighbors
def solve_15_puzzle(start, goal):
    pq = []
    g = 0
    h = manhattan(start, goal)
    heapq.heappush(pq, (g+h, g, start))
    visited = set()
    while pq:
        f, g, node = heapq.heappop(pq)
        state = tuple(tuple(row) for row in node)
        if state in visited:
            continue
        visited.add(state)
        if node == goal:
            return g
        for nxt in get_neighbors(node):
            t = tuple(tuple(row) for row in nxt)
            if t not in visited:
                heapq.heappush(pq, (g+1 + manhattan(nxt, goal), g+1, nxt))

    return -1
start = [
    [1, 2, 3, 4],
    [5, 6, 0, 8],
    [9,10,7,11],
    [13,14,15,12]
]
goal = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9,10,11,12],
    [13,14,15,0]
]
print("Moves required:", solve_15_puzzle(start, goal))