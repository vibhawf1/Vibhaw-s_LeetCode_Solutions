class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        directions = {1: (0, 1), 2: (0, -1), 3: (1, 0), 4: (-1, 0)}
        remaining_directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        m, n = len(grid), len(grid[0])

        inbound = lambda r,c : 0 <= r < m and 0 <= c < n
        visited = {(0, 0): 0}
        valid = lambda r, c, cost: (r, c) not in visited or cost < visited[(r, c)]

        heap = []
        heappush(heap, (0, 0, 0))

        while heap:
            cost, row, col = heappop(heap)
            if (row, col) == (m - 1, n - 1):
                return cost
            
            nr, nc = directions[grid[row][col]]
            next_row, next_col = nr + row, nc + col
            if inbound(next_row, next_col) and valid(next_row, next_col, cost):
                visited[(next_row, next_col)] = cost
                heappush(heap, (cost, next_row, next_col))
            
            for r, c in remaining_directions:
                if (r, c) == (nr, nc):
                    continue
                cr, cc = r + row, c + col
                if inbound(cr, cc) and valid(cr, cc, cost + 1):
                    visited[(cr, cc)] = cost + 1
                    heappush(heap, (cost + 1, cr, cc))
        
        return -1


        
