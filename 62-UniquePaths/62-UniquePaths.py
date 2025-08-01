# Last updated: 8/1/2025, 9:46:40 PM
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        def dp(i, j):
            if i >= m or j >= n:
                return 0
            if i == m - 1 and j == n - 1:
                return 1
            if (i, j) in memo:
                return memo[(i, j)]
            
            memo[(i, j)] = dp(i + 1, j) + dp(i, j + 1)
            
            return memo[(i, j)]

        return dp(0, 0)