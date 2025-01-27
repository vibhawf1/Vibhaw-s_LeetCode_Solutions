class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Build the adjacency list representation of the graph
        graph = [[] for _ in range(numCourses)]
        for pre, course in prerequisites:
            graph[course].append(pre)

        # Use depth-first search (DFS) to check if a course is a prerequisite
        def dfs(start, target):
            if start == target:
                return True
            visited[start] = True
            for neighbor in graph[start]:
                if not visited[neighbor] and dfs(neighbor, target):
                    return True
            return False

        # Iterate over the queries and check each one
        answer = []
        for u, v in queries:
            visited = [False] * numCourses
            answer.append(dfs(v, u))  # Check if u is reachable from v

        return answer
