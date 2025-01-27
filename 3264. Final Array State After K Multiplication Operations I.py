class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            min_index = nums.index(min(nums))  # Find the index of the first minimum element
            nums[min_index] *= multiplier  # Multiply the minimum element by the multiplier
        return nums 
