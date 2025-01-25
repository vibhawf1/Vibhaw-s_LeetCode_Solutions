class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        els = list(sorted([(nums[i], i) for i in range(len(nums))]))

        
        part = [els[0]]
        parts = []
        for i in range(1, len(els)):
            if els[i][0] - els[i-1][0] <= limit:
                part.append(els[i])
            else:
                parts.append(part)
                part = [els[i]]
        
        parts.append(part)

        result = [None for _ in range(len(nums))]

        for part in parts:
            indexes = sorted(map(lambda x:x[1], part))
            values = sorted(map(lambda x:x[0], part))
            for ii in range(len(indexes)):
                result[indexes[ii]] = values[ii]
        return result
