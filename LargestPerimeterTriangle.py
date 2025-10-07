from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # Step 1: Sort the array in ascending order.
        nums.sort()
        
        # Step 2: Iterate from the end of the array.
        # We need at least 3 elements, so we go down to index 2.
        for i in range(len(nums) - 1, 1, -1):
            # Let a, b, c be the three sides
            c = nums[i]
            b = nums[i-1]
            a = nums[i-2]
            
            # Step 3: Check the triangle inequality theorem.
            if a + b > c:
                # If it's a valid triangle, this is the largest possible perimeter.
                return a + b + c
        
        # Step 4: If the loop finishes, no valid triangle was found.
        return 0