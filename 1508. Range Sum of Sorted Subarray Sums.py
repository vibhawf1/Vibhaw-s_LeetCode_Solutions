class Solution(object):
    def rangeSum(self, nums, n, left, right):
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        
        minHeap = []

        for i in range(1, n + 1):
            for j in range(i):
                heapq.heappush(minHeap, prefix[i] - prefix[j])
        
        result = 0
        for i in range(1, right + 1):
            sum_value = heapq.heappop(minHeap)
            if i >= left:
                result = (result + sum_value) % 1000000007
        
        return result
