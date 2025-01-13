class Solution:
    def reverse(self, x: int) -> int:
        arr = []
        should_reverse = x < 0
        if should_reverse:
            x *= -1
        while (x // 10 > 0):
            base = x % 10
            arr.append(base)
            x = x // 10
        arr.append(x)
        sum = 0
        for i in range(len(arr)):
            sum += ((10**(len(arr) - i - 1)) * arr[i])
        if should_reverse:
            sum *= -1
        meets_constraints = -2**31 <= sum and sum <= 2**31 - 1
        return sum if meets_constraints else 0

        
