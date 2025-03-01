class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[2] * n for _ in range(n)]  # Initialize with 2 (minimum length)
        index = {x: i for i, x in enumerate(arr)}  # Store indices for quick lookup
        max_len = 0

        for k in range(2, n):
            for j in range(k - 1, 0, -1):
                diff = arr[k] - arr[j]
                if diff in index and index[diff] < j:
                    i = index[diff]
                    dp[j][k] = dp[i][j] + 1  # Extend the subsequence
                    max_len = max(max_len, dp[j][k])

        return max_len if max_len > 2 else 0  # If no subsequence longer than 2
