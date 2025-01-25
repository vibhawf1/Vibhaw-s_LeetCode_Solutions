class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # In a star graph, the center node is part of every edge.
        # So, we just need to find the common node in the first two edges.
        return edges[0][0] if edges[0][0] in edges[1] else edges[0][1] 
