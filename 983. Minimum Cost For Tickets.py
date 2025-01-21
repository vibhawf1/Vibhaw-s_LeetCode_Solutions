class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [float('inf')] * (days[-1] + 1)  # dp[i] represents the min cost to cover days up to i
        dp[0] = 0
        dayset = set(days)

        for i in range(1, days[-1] + 1):
            if i not in dayset:
                dp[i] = dp[i - 1]  # No need to buy a ticket if we're not traveling
            else:
                dp[i] = min(
                    dp[i - 1] + costs[0],  # Buy a 1-day pass
                    dp[max(0, i - 7)] + costs[1],  # Buy a 7-day pass
                    dp[max(0, i - 30)] + costs[2]  # Buy a 30-day pass
                )

        return dp[days[-1]]
