class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        # Initialize variables to track positions
        last_out_of_bounds = -1  # Position of last element outside [minK, maxK]
        last_min = -1            # Position of last occurrence of minK
        last_max = -1            # Position of last occurrence of maxK
        result = 0               # Count of valid subarrays
        
        for i, num in enumerate(nums):
            # Check if current number is within bounds
            if num < minK or num > maxK:
                # Mark this as an invalid position
                last_out_of_bounds = i
            
            # Update positions of minK and maxK
            if num == minK:
                last_min = i
            if num == maxK:
                last_max = i
            
            # Count valid subarrays ending at position i
            # The start point can be anywhere between last_out_of_bounds+1 and min(last_min, last_max)
            valid_start_points = min(last_min, last_max) - last_out_of_bounds
            
            # Add valid subarrays to result if both minK and maxK have been found
            if last_min > last_out_of_bounds and last_max > last_out_of_bounds:
                result += valid_start_points
        
        return result
