from typing import List

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 1  # At least one group is needed
        group_min = nums[0]

        for num in nums:
            if num - group_min > k:
                count += 1
                group_min = num  # Start a new group

        return count
