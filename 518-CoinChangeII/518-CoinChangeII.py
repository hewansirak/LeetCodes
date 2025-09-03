# Last updated: 9/3/2025, 11:49:14 PM
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0 for _ in range(n+1)] for _ in range(amount+1)]
        
        for i in range(amount):
            dp[i][n] = 0
        for i in range(n+1):
            dp[0][i] = 1
        
        for target in range(1, amount+1):
            for i in range(n-1,-1,-1):
                if target - coins[i] < 0:
                    dp[target][i] = dp[target][i+1]
                else:
                    dp[target][i] = dp[target][i+1] + dp[target-coins[i]][i]
        print(dp)
        return dp[amount][0]