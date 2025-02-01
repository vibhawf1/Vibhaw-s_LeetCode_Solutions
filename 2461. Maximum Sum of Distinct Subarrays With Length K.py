from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_sum = 0
        current_sum = 0
        unique_elements = set()
        left = 0

        for right in range(len(nums)):
            # If the current element is already in the set, move the left pointer
            while nums[right] in unique_elements:
                unique_elements.remove(nums[left])
                current_sum -= nums[left]
                left += 1

            # Add the current element to the set and update the sum
            unique_elements.add(nums[right])
            current_sum += nums[right]

            # If the window size is k, check if all elements are distinct
            if right - left + 1 == k:
                if len(unique_elements) == k:
                    max_sum = max(max_sum, current_sum)
                # Move the window: remove the leftmost element
                unique_elements.remove(nums[left])
                current_sum -= nums[left]
                left += 1

        return max_sum
