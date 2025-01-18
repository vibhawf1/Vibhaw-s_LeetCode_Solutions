class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        unique_cnt = 1
        last_unique_num = nums[0] - k   # Smallest number minus k

        for n in nums[1:]:   # Slicing
            next_num = max( last_unique_num+1 , n-k )
            if next_num <= n+k:
                last_unique_num = next_num
                unique_cnt += 1
        
        return unique_cnt
