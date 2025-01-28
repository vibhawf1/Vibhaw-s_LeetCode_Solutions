class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_fish = 0

        def dfs(row, col):
            if row < 0 or row >= m or col < 0 or col >= n or grid[row][col] == 0:
                return 0
            fish = grid[row][col]
            grid[row][col] = 0  # Mark the cell as visited by setting it to 0
            fish += dfs(row + 1, col)
            fish += dfs(row - 1, col)
            fish += dfs(row, col + 1)
            fish += dfs(row, col - 1)
            return fish

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    max_fish = max(max_fish, dfs(i, j))
        return max_fish
