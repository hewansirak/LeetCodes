# Last updated: 8/8/2025, 10:17:24 PM
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        memo = [[-1 for _ in range(n)] for _ in range(m)]

        def dp(i, j):
            if i == m or j == n:
                return 0
            if memo[i][j] != -1:
                return memo[i][j]
            
            if text1[i] == text2[j]:
                memo[i][j] = 1 + dp(i + 1, j + 1)
            else:
                memo[i][j] = max(dp(i + 1, j), dp(i, j + 1))
            
            return memo[i][j]

        return dp(0, 0)