class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        
        @cache
        def fn(mask, rem):
            """Return minimum work sessions to finish tasks indicated by set bits in mask."""
            if not mask: return 0 # done 
            ans = inf 
            for i, x in enumerate(tasks): 
                if mask & (1<<i): 
                    if x <= rem: ans = min(ans, fn(mask ^ (1<<i), rem - x))
                    else: ans = min(ans, 1 + fn(mask ^ (1<<i), sessionTime - x))
            return ans
        
        return fn((1<<len(tasks))-1, 0)
