class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        max_sum = current_sum = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                current_sum += nums[i]
            else:
                max_sum = max(max_sum, current_sum)
                current_sum = nums[i]
        
        # Final check in case the last subarray is the maximum
        max_sum = max(max_sum, current_sum)
        
        return max_sum
