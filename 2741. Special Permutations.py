class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        @lru_cache(None)
        def dfs(node,path):
            path|=(1<<node)
            if path==(2**m)-1: return 1
            res=0
            for nxt in g[node]:
                if not (path & (1<<nxt)):
                    res+=dfs(nxt,path)
                    res%=(10**9+7)
            return res

        m=len(nums)
        g=defaultdict(list)
        for i in range(m):
            for j in range(i+1,m):
                if nums[i]%nums[j]==0 or nums[j]%nums[i]==0:
                    g[i].append(j)
                    g[j].append(i)
        
        res=0
        for i in range(m):
            res+=dfs(i,0)
            res%=(10**9+7)
        return res
                
