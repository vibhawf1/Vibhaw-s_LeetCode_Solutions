from collections import deque,defaultdict
class Solution:
    def bfs(self, adj_list , start,target , n):
        visited = [False] * n
        node_queue = deque()
        node_queue.append(start)
        level_cnt = 0
        while node_queue:
            node_queue_len = len(node_queue)
            for _ in range(node_queue_len):
                node = node_queue.popleft()
                if visited[node]:
                    continue
                if node == target:
                    return level_cnt
                for neib in adj_list[node]:
                    node_queue.append(neib)  
                visited[node] = True
            level_cnt+=1
                  

    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:        
        adj_list = defaultdict(list)
        for i in range(0,n-1):
            adj_list[i].append(i+1)
        ans = []
        for u , v in queries:
            adj_list[u].append(v)
            ans.append(self.bfs(adj_list , 0 , n-1 , n))
        
        return ans
