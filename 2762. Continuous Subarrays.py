from sortedcontainers import SortedList
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        slist = SortedList()
        i,j = 0, 0
        n = len(nums)
        count = 0
        while(j<n):
            slist.add(nums[j])
            mini = slist[0]
            maxi = slist[-1]
            while(i<j and abs(maxi-mini) > 2):
                slist.remove(nums[i])
                i+=1
                maxi = slist[-1]
                mini = slist[0]
            count += j - i + 1
            j+=1
        
        return count
