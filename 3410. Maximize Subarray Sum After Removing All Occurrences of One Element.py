class Solution:
    def maxSubarraySum(self, nums: List[int]) -> int:
        if max(nums) <= 0:
            return max(nums)

        def solve(nums):
            prefix_sums = list(accumulate(nums, initial=0))
            dp = [0] * len(nums)
            most_recent = {}
            s = 0
            for i, v in enumerate(nums):
                if v < 0:
                    if v in most_recent:
                        connect = prefix_sums[i] - prefix_sums[most_recent[v]+1] + dp[most_recent[v]]
                        dp[i] = max(s, connect)
                    else:
                        dp[i] = s
                    most_recent[v] = i
                s = max(0, s + v)      
            return dp

        ans0, ans1 = -inf, -inf
        s = 0
        for v in nums:
            s = s + v if s > 0 else v
            ans0 = max(ans0, s)
            
        forward, backward = solve(nums), solve(nums[::-1])[::-1]
        ans1 = max(forward[i] + backward[i] for i in range(len(nums)))
        return max(ans0, ans1)
            
