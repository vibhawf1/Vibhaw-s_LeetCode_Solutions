class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        xor1 = 0  # XOR of all elements in nums1
        xor2 = 0  # XOR of all elements in nums2

        # Compute XOR for nums1
        for num in nums1:
            xor1 ^= num
            
        # Compute XOR for nums2
        for num in nums2:
            xor2 ^= num

        # Determine final result based on parity of lengths
        result = (xor2 if len(nums1) % 2 != 0 else 0) ^ (
            xor1 if len(nums2) % 2 != 0 else 0
        )

        return result
