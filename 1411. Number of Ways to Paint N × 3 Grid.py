from typing import List

class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7

        # For n = 1:
        # abc_count: number of ways to paint a 1x3 grid where all 3 colors are different (e.g., RYG).
        # There are 3! = 6 such patterns.
        abc_count = 6 
        
        # aba_count: number of ways to paint a 1x3 grid where first and third colors are same, middle is different (e.g., RYR).
        # There are 3 choices for the repeated color and 2 for the middle. So, 3 * 2 = 6 such patterns.
        aba_count = 6

        # Iterate from n = 2 up to the given n to build up the DP values
        for _ in range(2, n + 1):
            # Calculate next_abc_count (current row is ABC type):
            # It can follow a previous ABC row in 2 ways.
            # It can follow a previous ABA row in 2 ways.
            next_abc_count = (2 * abc_count + 2 * aba_count) % MOD

            # Calculate next_aba_count (current row is ABA type):
            # It can follow a previous ABC row in 2 ways.
            # It can follow a previous ABA row in 3 ways.
            next_aba_count = (2 * abc_count + 3 * aba_count) % MOD
            
            # Update counts for the next iteration
            abc_count = next_abc_count
            aba_count = next_aba_count
        
        # The total number of ways for n rows is the sum of ways ending with an ABC pattern
        # and ways ending with an ABA pattern.
        return (abc_count + aba_count) % MOD
