class Solution:
    def subarraySum(self, nums: List[int]) -> int:

        result = 0

        for index in range(len(nums)):
            
            result = result + sum(nums[max(0,index - nums[index]) :index +1]) 

        return result
