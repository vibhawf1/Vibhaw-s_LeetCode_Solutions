class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:

        ops = 0

        for j in range(len(grid[0])):
            for i in range(1,len(grid)):

                if grid[i-1][j] >= grid[i][j]:
                    ops+= grid[i-1][j] - grid[i][j] + 1
                    grid[i][j] += grid[i-1][j] - grid[i][j] + 1


        return ops

                   
