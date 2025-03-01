class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_so_far = 0
        min_so_far = 0
        max_abs_sum = 0

        for num in nums:
            max_so_far = max(num, max_so_far + num)
            min_so_far = min(num, min_so_far + num)
            max_abs_sum = max(max_abs_sum, max_so_far, abs(min_so_far))

        return max_abs_sum
