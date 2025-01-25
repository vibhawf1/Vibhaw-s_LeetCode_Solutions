class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)  # For efficient checking
        count = 0
        current_sum = 0

        for i in range(1, n + 1):
            if i in banned:
                continue  # Skip banned numbers
            if current_sum + i <= maxSum:
                count += 1
                current_sum += i
            else:
                break  # Stop if adding the next number exceeds maxSum

        return count
