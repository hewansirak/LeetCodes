# Last updated: 9/20/2025, 11:47:58 PM
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        
        def dfs(target):
            if target == 0:
                return 1
            if target in memo:
                return memo[target]

            count = 0
            for num in nums:
                if num <= target:
                    count += dfs(target-num)
            memo[target] = count
            return memo[target]

        return dfs(target)
        