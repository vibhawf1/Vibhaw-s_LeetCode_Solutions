class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        
        # Shift all 0's to the end
        left = 0
        for right in range(n):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        
        return nums
