class Solution(object):
    def maximumCoins(self, coins, k):
        coins.sort(key=lambda x: x[0])

        xx = [-int(1e10)]
        cc = [0]

        ss = 0

        for l,r,c in coins:
            xx += [l]
            cc += [ss]
            
            ss += (r - l + 1) * c

            xx += [r+1]
            cc += [ss]

        xx += [int(1e10)]
        cc += [ss]

        def left_sum(i):
            j = bisect_left(xx, xx[i] - k)

            x1 = xx[i]
            x2 = xx[j]
            x3 = xx[j-1]

            c1 = cc[i]
            c2 = cc[j]
            c3 = cc[j-1]

            xd = max(0, k - (x1 - x2))
            cd = (c2 - c3) // (x2 - x3)

            return (c1 - c2) + xd*cd
        
        def right_sum(i):
            j = bisect_left(xx, xx[i] + k)

            x1 = xx[i]
            x2 = xx[j-1]
            x3 = xx[j]

            c1 = cc[i]
            c2 = cc[j-1]
            c3 = cc[j]
            
            xd = max(0, k - (x2 - x1))
            cd = (c3 - c2) // (x3 - x2)

            return (c2 - c1) + xd*cd

        res = 0

        for i in range(1,len(xx)-1):
            res = max(res, left_sum(i), right_sum(i))
     
        return res
