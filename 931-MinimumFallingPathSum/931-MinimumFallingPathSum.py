# Last updated: 9/5/2025, 11:13:37 PM
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])

        dp = [[0] * m for i in range(n)]

        for j in range(m):
            dp[0][j] = matrix[0][j]
        
        for i in range(1,n):
            for j in range(m):
                up = matrix[i][j] + dp[i-1][j]
                dl = dr = float("inf")
                if j + 1 < m:
                    dl = matrix[i][j] + dp[i-1][j+1]
                if j - 1 >= 0:
                    dr = matrix[i][j] + dp[i-1][j-1]
                dp[i][j] = min(up, dl, dr)
        
        mini = float('inf')
        for j in range(m):
            mini = min(mini, dp[n-1][j])
        return mini