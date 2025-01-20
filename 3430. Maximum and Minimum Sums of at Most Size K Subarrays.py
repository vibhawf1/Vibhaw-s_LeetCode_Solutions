class Solution:
    def minMaxSubarraySum(self, nums: List[int], k: int) -> int:
        stack1 = []
        stack2 = []
        n = len(nums)
        nl = [n for i in range(n)]
        bl = [-1 for i in range(n)]
        ns = [n for i in range(n)]
        bs = [-1 for i in range(n)]
        for i in range(n):
            while stack1 and nums[stack1[-1]] <= nums[i]:
                nl[stack1[-1]] = i
                stack1.pop()
            stack1.append(i)
            while stack2 and nums[stack2[-1]] >= nums[i]:
                ns[stack2[-1]] = i
                stack2.pop()
            stack2.append(i)
        stack1 = []
        stack2 = []
        for i in range(n-1,-1,-1):
            while stack1 and nums[stack1[-1]] < nums[i]:
                bl[stack1[-1]] = i
                stack1.pop()
            stack1.append(i)
            while stack2 and nums[stack2[-1]] > nums[i]:
                bs[stack2[-1]] = i
                stack2.pop()
            stack2.append(i)
        res = 0
        @cache
        def choices(l,r):
            l = min(l,k)
            r = min(r,k)
            res = l*r
            if l+r-1<=k:return l*r #% (10**9+7)
            for ll in range(l,-1,-1):
                if ll + r - 1 <= k:break
                res -= ll+r-1 - k 
            return res


        for i,a in enumerate(nums):
            R1 = nl[i] - i 
            L1 = i - bl[i]
            R2 = ns[i] - i
            L2 = i - bs[i]
            res += a*(choices(L1,R1)+choices(L2,R2))# % (10**9+7)
        return res
