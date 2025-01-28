from typing import List

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        # Build the adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # Initialize the count of valid components
        self.count = 0
        
        # DFS function to traverse the tree and calculate subtree sums
        def dfs(node, parent):
            total = values[node]
            for neighbor in adj[node]:
                if neighbor != parent:
                    total += dfs(neighbor, node)
            if total % k == 0:
                self.count += 1
            return total
        
        # Start DFS from the root (node 0)
        dfs(0, -1)
        
        return self.count
