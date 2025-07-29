# Last updated: 7/29/2025, 11:10:01 PM
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [-1] * n

        def dp(i):
            if i >= n:
                return 0


            if memo[i] != -1:
                return memo[i]
            rob_current = nums[i] + dp(i + 2)

            skip_current = dp(i + 1)

            memo[i] = max(rob_current, skip_current)
            return memo[i]

        return dp(0)
