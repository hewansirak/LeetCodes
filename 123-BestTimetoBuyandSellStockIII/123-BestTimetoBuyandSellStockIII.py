# Last updated: 8/16/2025, 11:25:26 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        dp = [[[ -1 for _ in range(2)] for _ in range(3)] for _ in range(len(prices) + 1)]
        def dfs(day, trans,buy):
            #  base case
            if day >= len(prices):
                return 0
            if trans == 0:
                return 0
            if dp[day][trans][buy] != -1:
                return dp[day][trans][buy]

            # if we buy sth already 
            #  we have to decide about sell day
            if buy:
                sell = prices[day] + dfs(day + 1, trans - 1, not buy)
                not_sell = dfs(day + 1, trans, buy)
                dp[day][trans][buy] =  max(sell, not_sell)
                return dp[day][trans][buy]
            else:
                #  we have to 
                buy_ = - prices[day] + dfs(day + 1, trans, not buy)
                not_buy = dfs(day + 1, trans, buy)
                dp[day][trans][buy] =  max(not_buy, buy_)
                return dp[day][trans][buy]

        return dfs(0, 2, False)

        