class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        left, right = 1, max(quantities)  # Binary search on the possible maximum

        def can_distribute(max_products):
            stores_needed = 0
            for q in quantities:
                stores_needed += (q + max_products - 1) // max_products  # Calculate stores needed for each product type
            return stores_needed <= n

        while left < right:
            mid = (left + right) // 2
            if can_distribute(mid):
                right = mid  # Try a smaller maximum
            else:
                left = mid + 1  # Need a larger maximum

        return left
