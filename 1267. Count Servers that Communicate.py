class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        servers_in_row = [0] * rows
        servers_in_col = [0] * cols
        
        # Count servers in each row and column
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    servers_in_row[i] += 1
                    servers_in_col[j] += 1
        
        # Count servers that can communicate
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (servers_in_row[i] > 1 or servers_in_col[j] > 1):
                    count += 1
        
        return count
