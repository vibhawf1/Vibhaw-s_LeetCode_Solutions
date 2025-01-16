class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target)]

        for num in candidates:
            if target - num < 0:
                continue

            dp[num - 1].append([num])
            for i in range(target - num):
                for comb in dp[i]:
                    dp[i + num].append(comb + [num])

        return dp[-1]
        
