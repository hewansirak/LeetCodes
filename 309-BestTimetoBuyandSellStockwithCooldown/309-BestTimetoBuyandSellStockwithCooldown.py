# Last updated: 8/18/2025, 11:51:15 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = {}

        def dp(i, holding):
            if i >= n:
                return 0
            if (i, holding) in memo:
                return memo[(i, holding)]

            if holding:
                # Sell or hold
                sell = prices[i] + dp(i+2, 0) 
                hold = dp(i+1, 1)
                memo[(i, holding)] = max(sell, hold)
            else:
                # Buy or skip
                buy = -prices[i] + dp(i+1, 1)
                skip = dp(i+1, 0)
                memo[(i, holding)] = max(buy, skip)

            return memo[(i, holding)]

        return dp(0, 0)