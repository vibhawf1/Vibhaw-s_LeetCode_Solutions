class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        num_ind = []
        for i, num in enumerate(nums):
            num_ind.append((num, i))
        
        num_ind.sort()
        
        count = len(num_ind)
        cur_cnt = 0
        for i in range(1, len(num_ind)):
            if num_ind[i][1] < num_ind[i-1][1]:
                cur_cnt += 1
            count += cur_cnt
        
        return count
                
