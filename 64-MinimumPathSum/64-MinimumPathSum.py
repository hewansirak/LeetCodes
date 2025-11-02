# Last updated: 11/2/2025, 10:13:41 PM
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0]) 
        dp = [float('inf')] * m
        dp[0] = 0

        for i in range(n):
            dp[0] += grid[i][0]
            for j in range(1, m):
                up = dp[j]
                left = dp[j - 1]
                dp[j] = min(up, left) + grid[i][j]

        return dp[-1]

        return self.min_sum