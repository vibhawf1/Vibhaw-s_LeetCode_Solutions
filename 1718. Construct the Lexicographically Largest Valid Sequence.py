from typing import List

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        result = [0] * (2 * n - 1)
        visited = [False] * (n + 1)

        def dfs(index: int) -> bool:
            if index == len(result):
                return True

            if result[index] != 0:  # Already filled, move to next index
                return dfs(index + 1)

            for num in range(n, 0, -1):
                if not visited[num]:
                    if num == 1:  # Handle '1' separately as it doesn't have a distance constraint
                        result[index] = num
                        visited[num] = True
                        if dfs(index + 1):
                            return True
                        result[index] = 0  # Backtrack
                        visited[num] = False
                    else:
                        next_index = index + num
                        if next_index < len(result) and result[next_index] == 0:
                            result[index] = num
                            result[next_index] = num
                            visited[num] = True
                            if dfs(index + 1):
                                return True
                            result[index] = 0  # Backtrack
                            result[next_index] = 0
                            visited[num] = False
            return False  # No valid number can be placed

        dfs(0)
        return result
