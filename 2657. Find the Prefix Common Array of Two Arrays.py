class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        AMASK = 0
        BMASK = 0
        ans = []
        for i in range(len(A)):
            AMASK |= 1 << A[i]
            BMASK |= 1 << B[i]
            ans.append(bin(AMASK & BMASK).count('1'))
        return ans
