# Last updated: 7/25/2025, 11:00:29 PM
class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        prefix_sum = [0]
        for value in sorted(coins):
            prefix_sum.append(prefix_sum[-1] + value)
        coins.sort()
        ans = 0

        for index in range(len(coins)):
            if -1 * (prefix_sum[index] - coins[index]) <= 1:
                ans = prefix_sum[index + 1]
            else:
                break
        return ans + 1