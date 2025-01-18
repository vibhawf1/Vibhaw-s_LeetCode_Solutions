class Solution:
    def subsequencesWithMiddleMode(self, nums: List[int]) -> int:
        n, mod = len(nums), 10**9+7
        pref, suff = Counter(), Counter(nums)
        nC2 = lambda x: x * (x-1) // 2

        # sum of pref[num] * (pref[num]-1) // 2, choose two identical elements from the left
        sum1 = 0
        # sum of suff[num] * (suff[num]-1) // 2, choose two identical elements from the right
        sum2 = sum(nC2(cnt) for cnt in suff.values())
        # sum of pref[num] * suff[num], choose one element from each side
        sum3 = 0
        # sum of pref[num] * pref[num] * suff[num], choose two from the left and one from the right
        sum4 = 0
        # sum of pref[num] * suff[num] * suff[num], choose one from the left and two from the right
        sum5 = 0
        
        res = 0
        for i,mid in enumerate(nums):

            sum1 -= nC2(pref[mid])
            sum2 -= nC2(suff[mid])
            sum3 -= pref[mid]*suff[mid]
            sum4 -= pref[mid]*pref[mid]*suff[mid]
            sum5 -= pref[mid]*suff[mid]*suff[mid]

            suff[mid] -= 1

            # + One mid & one non-mid in the left and two distinct elements in the right
            # [1,3,3,4,5], [1,3,3,1,5], [1,3,3,3,5], [1,3,3,1,3]
            res += pref[mid] * (i-pref[mid]) * (nC2(n-i-1) - sum2)
            # + Two distinct elements in the right and One mid & one non-mid in the right
            # [1,2,3,3,5], [1,2,3,1,3], [1,3,3,3,5], [1,3,3,1,3]
            res += (nC2(i) - sum1) * (n-i-1 - suff[mid]) * suff[mid]

            # - One mid in the left and one non-mid in the right
            # [1,3,3,1,5], [1,3,3,3,3], [1,3,3,1,1]
            res -= pref[mid] * sum3 * (n-i-1 - suff[mid])
            # - One non-mid in the left and one mid in the right
            # [1,2,3,1,3], [1,3,3,3,3], [1,1,3,3,1]
            res -= (i-pref[mid]) * sum3 * suff[mid]

            # + One mid in the left
            # [1,3,3,1,1], [3,3,3,3,3]
            res += pref[mid] * sum5
            # + One mid in the right
            res += sum4 * suff[mid]

            # - One mid & one non-mid in the left and two mid in the right
            # [1,3,3,3,3]
            res -= pref[mid] * (i-pref[mid]) * nC2(suff[mid])
            # - One mid & one non-mid in the left and one mid & one non-mid in the right
            res -= pref[mid] * (i-pref[mid]) * (n-i-1 - suff[mid]) * suff[mid]

            # + Two mid in the left
            # [1,2,3,3,3], [1,1,3,3,3], [1,3,3,3,3], [3,3,3,3,3]
            res += nC2(pref[mid]) * nC2(n-i-1)
            # + Two mid in the right
            res += nC2(i) * nC2(suff[mid])

            # - Two mid in the left and one mid & one non-mid in the right
            # [3,3,3,3,5]
            res -= nC2(pref[mid]) * suff[mid] * (n-i-1 - suff[mid])
            # - Two mid on both sides
            # [3,3,3,3,3]
            res -= nC2(pref[mid]) * nC2(suff[mid])
            
            res %= mod

            pref[mid] += 1

            sum1 += nC2(pref[mid])
            sum2 += nC2(suff[mid])
            sum3 += pref[mid] * suff[mid]
            sum4 += pref[mid] * pref[mid] * suff[mid]
            sum5 += pref[mid] * suff[mid] * suff[mid]

        return res
