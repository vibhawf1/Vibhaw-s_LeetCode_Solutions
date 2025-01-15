class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = []
        if target in nums:
            result.append(nums.index(target))
            result.append(len(nums) - nums[::-1].index(target) - 1)
            return result
        else:
            return [-1,-1]
        
