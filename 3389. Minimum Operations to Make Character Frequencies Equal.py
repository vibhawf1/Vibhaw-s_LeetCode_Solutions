class Solution:
    def makeStringGood(self, s: str) -> int:
        hash = [0] * 26
        for c in s:
            hash[ord(c) - ord("a")] += 1

        max_freq = max(hash)
        memo = [dict() for _ in range(26)]

        def dp(i, f, dropped):
            if i >= 26:
                return 0

            if (f, dropped) in memo[i]:
                return memo[i][(f, dropped)]

            res = (
                dp(i + 1, f, 0)
                if hash[i] in {0, f}
                else (
                    # drop excess
                    hash[i] - f + dp(i + 1, f, hash[i] - f)
                    if hash[i] > f
                    else min(
                        # drop all
                        hash[i] + dp(i + 1, f, hash[i]),
                        # add deficit
                        max(f - (hash[i] + dropped), 0) + dp(i + 1, f, 0),
                    )
                )
            )

            memo[i][(f, dropped)] = res
            return res

        return min([dp(0, f, 0) for f in range(1, 1 + max(hash))])

        # O(n^1.5) time
        # O(n^1.5) space
