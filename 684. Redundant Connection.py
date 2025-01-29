class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges) + 1))  # Nodes are 1-based
        
        def find(u: int) -> int:
            while parent[u] != u:
                parent[u] = parent[parent[u]]  # Path compression
                u = parent[u]
            return u
        
        for u, v in edges:
            root_u = find(u)
            root_v = find(v)
            if root_u == root_v:
                return [u, v]
            parent[root_v] = root_u  # Union
        
        return []  # According to problem constraints, this line is unreachable
