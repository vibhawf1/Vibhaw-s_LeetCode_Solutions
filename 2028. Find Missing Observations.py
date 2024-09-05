class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        Total_sum = (len(rolls) + n)*mean - sum(rolls)
        if Total_sum < n or Total_sum > 6*n:
            return []
        ans = [1]*n
        remain_sum = Total_sum - n
        i = 0
        while(remain_sum > 0):
            increment = min(remain_sum, 5)
            ans[i] += increment
            remain_sum -= increment
            i += 1
        return ans       
