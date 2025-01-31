class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        def dfs(node, discovery_time, low_time, graph, visited, parent, result):
            visited[node] = True
            discovery_time[node] = low_time[node] = self.time
            self.time += 1
            
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if not visited[neighbor]:
                    dfs(neighbor, discovery_time, low_time, graph, visited, node, result)
                    low_time[node] = min(low_time[node], low_time[neighbor])
                    if low_time[neighbor] > discovery_time[node]:
                        result.append([node, neighbor])
                else:
                    low_time[node] = min(low_time[node], discovery_time[neighbor])

        graph = [[] for _ in range(n)]
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        self.time = 0
        visited = [False] * n
        discovery_time = [0] * n
        low_time = [0] * n
        result = []
        dfs(0, discovery_time, low_time, graph, visited, -1, result)
        return result
