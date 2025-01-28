from typing import List

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        
        # Step 1: Compute the sum of every subarray of length k
        window_sums = []
        current_sum = sum(nums[:k])
        window_sums.append(current_sum)
        
        for i in range(1, n - k + 1):
            current_sum = current_sum - nums[i - 1] + nums[i + k - 1]
            window_sums.append(current_sum)
        
        # Step 2: Compute the left array
        left = [0] * len(window_sums)
        best = 0
        for i in range(len(window_sums)):
            if window_sums[i] > window_sums[best]:
                best = i
            left[i] = best
        
        # Step 3: Compute the right array
        right = [0] * len(window_sums)
        best = len(window_sums) - 1
        for i in range(len(window_sums) - 1, -1, -1):
            if window_sums[i] >= window_sums[best]:
                best = i
            right[i] = best
        
        # Step 4: Find the optimal combination of three subarrays
        max_sum = 0
        result = []
        for mid in range(k, len(window_sums) - k):
            l = left[mid - k]
            r = right[mid + k]
            total = window_sums[l] + window_sums[mid] + window_sums[r]
            if total > max_sum:
                max_sum = total
                result = [l, mid, r]
        
        return result
