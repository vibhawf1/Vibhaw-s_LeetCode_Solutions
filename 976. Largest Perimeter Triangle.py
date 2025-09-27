from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        """
        Given an integer array nums, return the largest perimeter of a triangle with non-zero area,
        formed from three of these lengths. If it is impossible, return 0.

        Approach:
        - Sort the array in descending order.
        - Iterate through each triplet and check the triangle inequality.
        - Return the first valid perimeter found.
        """
        nums.sort(reverse=True)  # Sort in descending order

        # Check each triplet starting from the largest
        for i in range(len(nums) - 2):
            a, b, c = nums[i], nums[i+1], nums[i+2]
            # Check if the sides can form a triangle
            if b + c > a:
                return a + b + c  # Return the perimeter

        return 0  # No valid triangle found
