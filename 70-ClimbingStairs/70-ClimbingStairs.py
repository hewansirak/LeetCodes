# Last updated: 7/29/2025, 11:07:05 PM
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1] * (n + 1)

        def dp(i: int) -> int:
            if i == 0:
                return 1 
            if i == 1:
                return 1  
            if memo[i] != -1:
                return memo[i]

            memo[i] = dp(i - 1) + dp(i - 2)
            return memo[i]

        return dp(n)