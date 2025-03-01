class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n1, n2 = len(str1), len(str2)
        
        # 1. Find the Longest Common Subsequence (LCS)
        dp = [[""] * (n2 + 1) for _ in range(n1 + 1)]
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + str1[i - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], key=len)
        lcs = dp[n1][n2]
        
        # 2. Construct the Shortest Common Supersequence (SCS)
        i, j = 0, 0
        scs = ""
        for char in lcs:
            while str1[i] != char:
                scs += str1[i]
                i += 1
            while str2[j] != char:
                scs += str2[j]
                j += 1
            scs += char  # Add the common character
            i += 1
            j += 1
        
        # 3. Append remaining characters
        scs += str1[i:]
        scs += str2[j:]
        
        return scs
