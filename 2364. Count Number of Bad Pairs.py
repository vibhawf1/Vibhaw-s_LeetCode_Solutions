class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)

        # frequency of nums[i] - i
        freq = {}
        for i in range(n):
            temp = nums[i] - i
            freq[temp] = freq.get(temp, 0) + 1

        total_pairs = n * (n - 1) // 2
        good_pairs = 0

        for value, frequency in freq.items():
            if frequency > 1:
                good_pairs += frequency * (frequency - 1) // 2

        # bad_pairs = total_pairs - good_pairs
        return total_pairs - good_pairs
