class Solution:
    def maximumInvitations(self, favorite: list[int]) -> int:
        # [Credits to Neetcode on Youtube]
        # 1. Find longest cycle
        n = len(favorite)
        longest_cycle = 0
        visited = [0] * n  
        length_2_cycles = []

        for i in range(n):
            if visited[i] == 1:
                continue
            
            start, curr = i, i
            curr_set = set()

            while visited[curr] == 0:
                visited[curr] = 1
                curr_set.add(curr)
                curr = favorite[curr]
            
            if curr in curr_set:
                length = len(curr_set)
                while start != curr:
                    length -= 1
                    start = favorite[start]
                longest_cycle = max(longest_cycle, length)

                if length == 2:
                    length_2_cycles.append([curr, favorite[curr]])

        # 2. Find longest 2-cycle chain
        inverted = defaultdict(list)
        for dst, src in enumerate(favorite):
            inverted[src].append(dst)
        
        # pass in the it's partner to avoid counting 
        # it when find the length of chain
        def bfs(src, partner):
            q = deque([(src, 0)]) # (node, length)
            max_length = 0
            
            while q:
                node, length = q.popleft()
                if node == partner:
                    continue
                max_length = max(max_length, length)
                for nei in inverted[node]:
                    q.append((nei, length + 1))
            return max_length
        
        chain_sum = 0
        for n1, n2 in length_2_cycles:
            # n1 path + n2 path + the 2 partner node itself
            chain_sum += bfs(n1, n2) + bfs(n2, n1) + 2
        
        return max(chain_sum, longest_cycle)
