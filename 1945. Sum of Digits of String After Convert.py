class Solution:
    def getLucky(self, s: str, k: int) -> int:
        # Step 1: Convert the string to an integer representation
        num_str = ''.join(str(ord(char) - ord('a') + 1) for char in s)
        
        # Convert num_str to an integer
        num = sum(int(digit) for digit in num_str)
        
        # Step 2: Perform the transformation k times
        for _ in range(k - 1):
            num = sum(int(digit) for digit in str(num))
        
        return num
