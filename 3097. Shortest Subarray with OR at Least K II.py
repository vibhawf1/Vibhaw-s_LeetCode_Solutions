class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        ans, bitwise_or, left, cnt = inf, 0, 0, [0]*32
        for right, num in enumerate(nums):
            bitwise_or |= num
            i = 0
            while num > 0:
                cnt[i] += num % 2
                num //= 2
                i += 1
            while bitwise_or >= k and left <= right:
                ans = min(right - left + 1, ans)
                num, i = nums[left], 0
                while num > 0:
                    if num % 2:
                        cnt[i] -= 1
                        if not cnt[i]:
                            bitwise_or ^= 1 << i
                    num //= 2
                    i += 1
                left += 1
        return -1 if ans == inf else ans
