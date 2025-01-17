class Solution:
    def numberOfSubsequences(self, nums: List[int]) -> int:
        n=len(nums)
        start=deque()
        ans=0
        c=Counter()
        for r in range(n):
            for s in range(r+2,n):
                frac=nums[s]/nums[r]
                start.append((r,frac))
                c[frac]+=1

        for q in range(n):
            while start and start[0][0]<q+2:
                _,frac=start.popleft()
                c[frac]-=1
            for p in range(q-1):
                ans+=c[nums[p]/nums[q]]
        return ans
