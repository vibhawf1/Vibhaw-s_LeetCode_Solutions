class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        height = [[-1 for _ in range(n)] for _ in range(m)]
        q = [(i, j) for i in range(m) for j in range(n) if isWater[i][j]]

        for i, j in q:
            height[i][j] = 0

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        level = 1
        while q:
            next_q = []
            for i, j in q:
                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and height[ni][nj] == -1:
                        height[ni][nj] = level
                        next_q.append((ni, nj))
            q = next_q
            level += 1

        return height
