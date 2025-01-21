class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        top_sum = sum(grid[0])
        bottom_sum = 0
        ans = float('inf')

        for i in range(n):
            top_sum -= grid[0][i]
            ans = min(ans, max(top_sum, bottom_sum))  # Minimize the max points for the 2nd robot
            bottom_sum += grid[1][i]

        return ans
