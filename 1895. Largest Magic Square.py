class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        # Prefix sums for rows and columns
        rows = [list(accumulate(r, initial=0)) for r in grid]
        cols = [list(accumulate(c, initial=0)) for c in zip(*grid)]

        R, C = len(grid), len(grid[0])
        for sz in range(min(R, C), 0, -1):
            for r in range(R - sz + 1):
                for c in range(C - sz + 1):
                    ref = rows[r][c + sz] - rows[r][c]
                    if (all(rows[i][c + sz] - rows[i][c] == ref for i in range(r + 1, r + sz)) and    #rows except the 1st
                        all(cols[i][r + sz] - cols[i][r] == ref for i in range(c, c + sz)) and   # columns
                        sum(grid[r + i][c + i] for i in range(sz)) == ref and    #diagonal 1
                        sum(grid[r + i][c + sz - 1 - i] for i in range(sz)) == ref):   #diagonal 2
                        return sz
