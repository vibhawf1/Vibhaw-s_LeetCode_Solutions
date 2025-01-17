class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return 0
        res = 0
        curr = 0
        farthest = nums[curr]
        barrier = 0
        while True:
            for positions in range(curr,barrier+1):
                farthest = max(farthest, positions+nums[positions])
            if farthest>=n-1:
                return res+1
            curr = barrier+1
            barrier = farthest
            res+=1
