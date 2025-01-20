class Solution:
    def minMaxSums(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        MOD = 10**9 + 7

        factorial = [1] * (n + 1)
        for i in range(1, n + 1):
            factorial[i] = factorial[i - 1] * i % MOD
        invFactorial = [1] * (n + 1)
        invFactorial[-1] = pow(factorial[-1], -1, MOD)
        for i in reversed(range(1, n)):
            invFactorial[i] = invFactorial[i + 1] * (i + 1) % MOD

        def nCr(n, r):
            res = factorial[n] * invFactorial[n - r] * invFactorial[r] % MOD if n >= r else 0
            return res

        res = 0
        for size in range(1, k + 1):
            for i in range(n):
                minContrib = nCr(n - i - 1, size - 1) * nums[i] % MOD
                maxContrib = nCr(i, size - 1) * nums[i] % MOD
                res = (res + maxContrib + minContrib) % MOD
        return res
