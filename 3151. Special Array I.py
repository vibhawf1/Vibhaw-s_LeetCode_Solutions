from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        # Iterate through the array up to the second last element
        for i in range(len(nums) - 1):
            # Check if the current and next element have the same parity
            if (nums[i] % 2) == (nums[i + 1] % 2):
                return False
        # If all pairs have different parity, return True
        return True
