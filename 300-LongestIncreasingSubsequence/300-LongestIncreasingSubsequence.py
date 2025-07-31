# Last updated: 7/31/2025, 10:06:01 PM
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        memo = [[-1 for _ in range(n + 2)] for _ in range(n + 2)]

        def dp(idx, lastIdx):
            if idx == n:
                return 0
            
            if memo[idx][lastIdx] != -1:
                return memo[idx][lastIdx]
            
            if lastIdx >= n + 1 or nums[lastIdx] < nums[idx]:
                memo[idx][lastIdx] = max(1 + dp(idx + 1, idx), dp(idx + 1, lastIdx))
            else:
                memo[idx][lastIdx] = dp(idx + 1, lastIdx)
            
            return memo[idx][lastIdx]
            
        return dp(0, n + 1)