INF = 0x3fffffff

class Solution:
    def nearestPalindromic(self, n: str) -> str:
        if len(n) == 1:
            num = int(n)
            return str(num-1)

        hf = len(n)>>1
        prefix = n[:hf]
        prefixNum = int(prefix)

        rslts = ['9'*(len(n)-1), '1'+'0'*(len(n)-1)+'1']
        hf = len(n)>>1
        prefix = n[:hf]

        if len(n)&1:
            suffix = prefix[::-1]
            prefix += n[hf]
            rslts.append(prefix+suffix)

            num = int(prefix)
            high = str(num+1)
            if len(high) == len(prefix):
                suffix = high[:-1][::-1]
                rslts.append(high+suffix)

            if num > 1:
                low = str(num-1)
                if len(low) == len(prefix):
                    suffix = low[:-1][::-1]
                    rslts.append(low+suffix)

        else:
            suffix = prefix[::-1]
            num = int(prefix)
            rslts.append(prefix+suffix)

            high = str(num+1)
            if len(high) == len(prefix):
                suffix = high[::-1]
                rslts.append(high+suffix)

            if num > 1:
                low = str(num-1)
                if len(low) == len(prefix):
                    suffix = low[::-1]
                    rslts.append(low+suffix)

        ans = None
        minn = INF
        target = int(n)

        for rslt in rslts:
            num = int(rslt)
            diff = abs(num-target)
            if diff and (diff < minn or (diff == minn and num < ans)):
                ans = num
                minn = diff
            
        return str(ans)
