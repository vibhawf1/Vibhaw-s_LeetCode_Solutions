class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        # Helper function to calculate combinations (n choose k)
        def combination(n, k):
            if n < 0 or k < 0:
                return 0
            if k == 0:
                return 1
            
            res = 1
            for i in range(k):
                res = res * (n - i) // (i + 1)
            return res
        
        # Total ways to distribute n objects among 3 recipients (stars and bars)
        total = combination(n + 3 - 1, 3 - 1)
        
        # Subtract distributions where at least one child exceeds limit
        if n > limit:
            # Ways where one child exceeds limit
            total -= 3 * combination(n - limit - 1 + 3 - 1, 3 - 1)
        
        # Add back distributions where at least two children exceed limit
        if n > 2 * limit:
            # Ways where two children exceed limit
            total += 3 * combination(n - 2 * limit - 2 + 3 - 1, 3 - 1)
        
        # Subtract distributions where all three children exceed limit
        if n > 3 * limit:
            # Ways where three children exceed limit
            total -= combination(n - 3 * limit - 3 + 3 - 1, 3 - 1)
        
        return max(0, total)
