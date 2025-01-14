class Solution(object):
    def longestSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        M = max(nums)
        dp = [[0] * M for i in range(M + 1)]
        for i in range(len(nums) - 1, -1, -1):
            n = nums[i]
            for nt in range(1, M + 1):
                diff = abs(n - nt)
                dp[n][diff] = max(dp[n][diff], dp[nt][diff] + 1)
            for j in range(1, M):
                dp[n][j] = max(dp[n][j], dp[n][j - 1])

        return max([max(dp[i]) for i in range(M + 1)])
