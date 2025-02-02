class Solution:
    def check(self, nums: List[int]) -> bool:
        pivot_count = 0
        n = len(nums)
        
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                pivot_count += 1
        
        return pivot_count <= 1
