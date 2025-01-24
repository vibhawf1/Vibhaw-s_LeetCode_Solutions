class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe = [False] * n
        graph_reversed = [[] for _ in range(n)]
        in_degree = [0] * n

        for i, neighbors in enumerate(graph):
            for neighbor in neighbors:
                graph_reversed[neighbor].append(i)
                in_degree[i] += 1

        queue = deque([i for i in range(n) if in_degree[i] == 0])

        while queue:
            node = queue.popleft()
            safe[node] = True
            for neighbor in graph_reversed[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return [i for i, is_safe in enumerate(safe) if is_safe]
