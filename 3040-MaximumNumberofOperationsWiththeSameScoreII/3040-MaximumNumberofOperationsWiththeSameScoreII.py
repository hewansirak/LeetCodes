# Last updated: 10/10/2025, 11:58:41 PM
class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)
        
        def dp(i, last, target, memo):
            if (i, last) in memo:
                return memo[(i, last)]
                
            if i >= last:
                return 0
                
            mx = 0

            if i + 1 <= last and nums[i] + nums[i + 1] == target:
                cur = 1 + dp(i + 2, last, target, memo)
                mx = max(mx, cur)

            if i < last and nums[i] + nums[last] == target:
                cur = 1 + dp(i + 1, last - 1, target, memo)
                mx = max(mx, cur)

            if last - 1 >= i and nums[last] + nums[last - 1] == target:
                cur = 1 + dp(i, last - 2, target, memo)
                mx = max(mx, cur)

            memo[(i, last)] = mx
            return mx

        res = max(
            1 + dp(2, n - 1, nums[0] + nums[1], {}),
            1 + dp(1, n - 2, nums[0] + nums[-1], {}),
            1 + dp(0, n - 3, nums[-1] + nums[-2], {})
        )
        return res