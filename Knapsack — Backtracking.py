def knapsack_backtrack(weights, values, capacity):
    n = len(weights)
    best_value = 0
    def backtrack(i, current_weight, current_value):
        nonlocal best_value
        if i == n:
            best_value = max(best_value, current_value)
            return
        backtrack(i + 1, current_weight, current_value)
        if current_weight + weights[i] <= capacity:
            backtrack(i + 1,
                      current_weight + weights[i],
                      current_value + values[i])

    backtrack(0, 0, 0)
    return best_value
weights = [2, 3, 4, 5]
values  = [3, 4, 5, 6]
capacity = 5

print("Maximum value:", knapsack_backtrack(weights, values, capacity))