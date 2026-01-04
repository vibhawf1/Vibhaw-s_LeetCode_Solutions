from typing import List

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total_sum = 0
        # Iterate through each number in the input array
        for num in nums:
            divisors = []
            # Find divisors up to the square root of the number
            for i in range(1, int(num**0.5) + 1):
                if num % i == 0:
                    divisors.append(i)
                    # If i*i is not equal to num, it means i and num/i are distinct divisors
                    # We avoid adding the same divisor twice for perfect squares
                    if i * i != num:
                        divisors.append(num // i)
            
            # If a number has exactly four divisors, add their sum to the total_sum
            if len(divisors) == 4:
                total_sum += sum(divisors)
        
        return total_sum
