class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1

        lastIdx = len(nums) - 1
        l, r = 0, lastIdx

        while l <= r:
            m = (l + r) // 2

            if nums[m] <= nums[lastIdx] and nums[lastIdx] < target:
                r = m - 1
            elif nums[m] > nums[lastIdx] and target <= nums[lastIdx]:
                l = m + 1
            else:
                if nums[m] > target:
                    r = m - 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    return m
