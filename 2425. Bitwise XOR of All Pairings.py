class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        intervals = sorted((*x, i) for i, x in enumerate(intervals))
        @cache
        def dfs(i, k): 
            if i == n: return 0, []
            if k == 0: return 0, []
            l, r, w, index = intervals[i]
            v, a = dfs(i+1, k)
            j = bisect_left(intervals, r+1, key = lambda x: x[0])
            vv, aa = dfs(j, k-1)
            aa = aa[:]
            insort(aa, index)
            if w+vv > v or w+vv == v and aa < a: v, a = w+vv, aa
            return v, a
        return dfs(0, 4)[1]
