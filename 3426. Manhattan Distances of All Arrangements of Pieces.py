class Solution:
    def distanceSum(self, m: int, n: int, k: int) -> int:
        MOD = 10**9 + 7
        S = defaultdict(int)
        for i in range(max(m,n)):
            S[i+1] = S[i] + i*(i+1)//2
        D = defaultdict(int)
        for i in range(1,m+1):
            for j in range(1,n+1):
                D[i,j] = D[i-1,j]+(2*i-3+j)*j//2
        res = 0
        for i in range(1,m+1):
            for j in range(1,n+1):
                res += D[i,j]
        res = 2*res - S[m]*n - S[n]*m
        return (res*comb(m * n - 2, k - 2) % MOD)%MOD        
