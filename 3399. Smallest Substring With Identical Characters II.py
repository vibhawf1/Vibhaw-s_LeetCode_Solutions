class Solution:
    def minLength(self, s: str, numOps: int) -> int:

        def valid(len_str: int)-> bool:
            if len_str == 1:
                sm = sum(map(lambda x: sum(x) % 2, enumerate(s)))
                return min(sm, n - sm) <= numOps

            return sum(g//(len_str + 1) for g in grp_len) <= numOps    


        n = len(s)
        s = list(map(int,s))
        
        grp_len = [len(list(grp)) for _, grp in groupby(s)]
        return bisect_left(range(1, n + 1), True, key = valid) + 1
