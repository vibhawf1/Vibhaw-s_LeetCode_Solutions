from typing import List
from collections import defaultdict

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_count = defaultdict(int)
        n = len(nums)
        
        # Generate all possible products of pairs (a, b) where a != b
        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                product_count[product] += 1
        
        # Calculate the total number of tuples
        total = 0
        for count in product_count.values():
            if count >= 2:
                total += count * (count - 1) * 4
        
        return total
