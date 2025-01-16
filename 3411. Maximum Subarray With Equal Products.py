class Solution:
    def getfactors(self, n:int) -> Counter:
        r = Counter()
        div = 2
        while div*div <= n:
            if n%div == 0 :
                r[div]+=1
                n//=div
            else:
                div+=1
        r[n]+=1
        r[1] = 0 # non specific divisor we can ignore
        return r
    
    def maxLength(self, nums: List[int]) -> int:
        r = 2
        for start in range(len(nums)):
            divs = self.getfactors(nums[start]) 
            lcm = divs
            gcd = divs
            prod = divs
            for end in range(start+1, len(nums)):
                divs = self.getfactors(nums[end]) 
                prod = prod+divs
                gcd = gcd & divs
                lcm = lcm | divs
                if lcm+gcd == prod:
                    # print(start,end,r, prod,gcd,lcm)
                    r = max(r, end+1-start)
                else:
                    break
        return r
        
