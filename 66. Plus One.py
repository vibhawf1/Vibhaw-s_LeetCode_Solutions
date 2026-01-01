from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        # Iterate from the last digit to the first
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                # If the digit is less than 9, just increment it and we are done.
                digits[i] += 1
                return digits
            else:
                # If the digit is 9, set it to 0 and carry over 1 to the next position.
                digits[i] = 0
        
        # If we reach here, it means all digits were 9s (e.g., [9, 9, 9])
        # We need to prepend a 1 to the array and append the zeros.
        return [1] + digits
