# Last updated: 8/10/2025, 11:26:48 PM
class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}
        
        def dp(n):
            if n in memo:
                return memo[n]
            if n == 0:
                return 0
            elif n == 1 or n == 2:
                return 1
            else:
                result = dp(n - 1) + dp(n - 2) + dp(n - 3)
                memo[n] = result
                return result
        
        return dp(n)