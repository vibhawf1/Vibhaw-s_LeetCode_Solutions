class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        MOD = 10**9 + 7
        
        # dp[i][j][xor] represents the number of paths reaching cell (i, j)
        # with the XOR of values along the path being equal to 'xor'.
        dp = [[[0] * 16 for _ in range(n)] for _ in range(m)]
        
        # Initialize the base case for the starting cell (0, 0).
        dp[0][0][grid[0][0]] = 1
        
        for i in range(m):
            for j in range(n):
                for xor in range(16):  # Iterate through possible XOR values
                    if i > 0:
                        # Check if coming from the cell above is valid
                        dp[i][j][xor] += dp[i - 1][j][xor ^ grid[i][j]]
                    if j > 0:
                        # Check if coming from the cell to the left is valid
                        dp[i][j][xor] += dp[i][j - 1][xor ^ grid[i][j]]
                    dp[i][j][xor] %= MOD  # Modulo to prevent overflow
        
        return dp[m - 1][n - 1][k]  # Return the count of paths with XOR k
                                      # ending at the bottom-right cell
