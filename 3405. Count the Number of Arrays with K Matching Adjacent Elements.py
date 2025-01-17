class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        # there are comb(n-1, n-k-1) combinations where n-k-1 positions have a[i-1] != a[i]
        # there are m choices at first
        # the rest of choices is (m-1) ^ (n-k-1)
        # ans = comb(n-1, n-k-1) * m * (m-1) ^ (n-k-1)
        # where comb(n-1, n-k-1) = factorial(n-1) / factorial(n-k-1) / factorial((n-1) - (n-k-1))
        #                        = factorial(n-1) / factorial(n-k-1) / factorial(k)

        MOD = 10**9 + 7

        factorial = [1] * n
        for i in range(1, n):
            factorial[i] = factorial[i-1] * i % MOD
        
        invFactorial = [1] * n
        invFactorial[n-1] = pow(factorial[n-1], -1, MOD)
        for i in range(n-2, 1, -1):
            invFactorial[i] = invFactorial[i+1] * (i+1) % MOD

        return factorial[n-1] * invFactorial[n-k-1] * invFactorial[k] * m * pow(m-1, n-k-1, MOD) % MOD
