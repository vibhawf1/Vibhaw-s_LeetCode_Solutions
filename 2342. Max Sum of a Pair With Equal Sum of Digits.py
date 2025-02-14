class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        max_sum = -1
        digit_sum_map = {}  # Store {digit_sum: max_num}

        for i, num in enumerate(nums):
            digit_sum = self.get_digit_sum(num)

            # If we've seen this digit sum before, update max_sum
            if digit_sum in digit_sum_map:
                max_sum = max(max_sum, num + digit_sum_map[digit_sum])
                # Update the stored number to the larger one for potential future pairs
                digit_sum_map[digit_sum] = max(digit_sum_map[digit_sum], num) 
            else:
                digit_sum_map[digit_sum] = num

        return max_sum

    def get_digit_sum(self, num: int) -> int:
        digit_sum = 0
        while num > 0:
            digit_sum += num % 10
            num //= 10
        return digit_sum
