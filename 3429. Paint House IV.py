class Solution:
    def minCost(self, n: int, cost: List[List[int]]) -> int:
        n = len(cost)
        ncost = []
        for i in range(n // 2):
            ncost.append([cost[i], cost[n - i - 1]])
        cost = ncost

        n = n // 2

        @cache
        def recur(i, a, b):
            if i == n:
                return 0

            ans = 999999999999
            for x in range(3):
                for y in range(3):
                    if x != a and y != b and x != y:
                        ans = min(ans, cost[i][0][x] + cost[i][1][y] + recur(i + 1, x, y))
            return ans

        return recur(0, -1, -1)
