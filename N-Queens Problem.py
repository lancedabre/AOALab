def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i] == j:
            return False
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i] == j:
            return False

    return True
def solve_n_queens_util(board, row, n, solutions):
    if row == n:
        solutions.append(board.copy())
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_n_queens_util(board, row + 1, n, solutions)
            board[row] = -1 
def solve_n_queens(n):
    board = [-1] * n
    solutions = []
    solve_n_queens_util(board, 0, n, solutions)
    return solutions
sol = solve_n_queens(4)
print("Number of solutions:", len(sol))
for s in sol:
    print(s)