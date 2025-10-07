from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        def findMaxSubArray(arr, low, high):
            # Base case: only one element
            if low == high:
                return arr[low]
            
            # Divide the array into two halves
            mid = (low + high) // 2
            
            # Conquer: find max sum in left and right subarrays
            left_max = findMaxSubArray(arr, low, mid)
            right_max = findMaxSubArray(arr, mid + 1, high)
            
            # Combine: find max sum of a crossing subarray
            cross_max = findMaxCrossingSubArray(arr, low, mid, high)
            
            # Return the maximum of the three
            return max(left_max, right_max, cross_max)

        def findMaxCrossingSubArray(arr, low, mid, high):
            # Find max subarray sum on the left side of mid
            left_sum = float('-inf')
            current_sum = 0
            for i in range(mid, low - 1, -1):
                current_sum += arr[i]
                if current_sum > left_sum:
                    left_sum = current_sum
            
            # Find max subarray sum on the right side of mid
            right_sum = float('-inf')
            current_sum = 0
            for i in range(mid + 1, high + 1):
                current_sum += arr[i]
                if current_sum > right_sum:
                    right_sum = current_sum
                    
            return left_sum + right_sum

        return findMaxSubArray(nums, 0, len(nums) - 1)