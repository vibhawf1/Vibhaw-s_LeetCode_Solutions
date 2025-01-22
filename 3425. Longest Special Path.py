class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        n = len(nums)
        adj = [[] for _ in range(n)]
        dp = [0] * n  # root To node path sum
        cnt = [1] * n # number of nodes from root to node

        for u, v, l in edges:
            adj[u].append((v, l))
            adj[v].append((u, l))

        def rootToNode(node, par):
            for nei, l in adj[node]:
                if nei == par:
                    dp[node] += dp[par] + l
                    cnt[node] += cnt[par]
                    break
            
            for nei, _ in adj[node]:
                if nei == par:
                    continue
                rootToNode(nei, node)
        
        rootToNode(0, -1)

        res = [0, 1]
        a = 0 # pointer from which the path has unique vals
        child = [-1] * n # immediate child of node in the current path
        seen = defaultdict(list)
        def dfs(node, par):
            nonlocal a
            val = nums[node]
            if val in seen:
                last = seen[val][-1] # bottom most node with same val in the current path
                if dp[child[last]] > dp[a]:
                    a = child[last]
            
            seen[val].append(node)

            pathSum = dp[node] - dp[a]
            node_cnt = cnt[node] - cnt[a] + 1
            if pathSum == res[0]:
                res[1] = min(res[1], node_cnt)
            elif pathSum > res[0]:
                res[0] = pathSum
                res[1] = node_cnt
            
            for nei, _ in adj[node]:
                if nei == par:
                    continue

                tmp_a = a
                child[node] = nei
                dfs(nei, node)
                child[node] = -1
                a = tmp_a
            
            seen[val].pop()
            if not seen[val]:
                seen.pop(val)
        
        dfs(0, -1)
        return res
