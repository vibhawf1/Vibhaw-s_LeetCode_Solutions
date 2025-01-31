class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def is_valid(row, col):
            return 0 <= row < n and 0 <= col < n

        def dfs(row, col, island_id):
            if not is_valid(row, col) or grid[row][col] != 1:
                return 0
            grid[row][col] = island_id
            area = 1
            for dx, dy in directions:
                area += dfs(row + dx, col + dy, island_id)
            return area

        # Step 1: Identify and label existing islands
        island_id = 2
        island_areas = {0: 0}  # Store island ID to its area
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    island_areas[island_id] = dfs(i, j, island_id)
                    island_id += 1

        # Step 2: Check for potential island merges
        max_area = max(island_areas.values())
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    neighbor_islands = set()
                    for dx, dy in directions:
                        if is_valid(i + dx, j + dy) and grid[i + dx][j + dy] > 1:
                            neighbor_islands.add(grid[i + dx][j + dy])
                    
                    potential_area = 1  # Start with the '0' we're changing
                    for island in neighbor_islands:
                        potential_area += island_areas[island]
                    max_area = max(max_area, potential_area)

        return max_area
