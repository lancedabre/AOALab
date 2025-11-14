def sum_of_subsets(nums, target):
    nums.sort()
    solutions = []
    subset = []
    def backtrack(i, current_sum):
        if current_sum == target:
            solutions.append(subset.copy())
            return
        if i >= len(nums) or current_sum > target:
            return
        subset.append(nums[i])
        backtrack(i + 1, current_sum + nums[i])
        subset.pop()
        backtrack(i + 1, current_sum)
    backtrack(0, 0)
    return solutions
nums = [3, 5, 6, 7]
target = 12
print("Subsets that sum to", target, ":")
print(sum_of_subsets(nums, target))