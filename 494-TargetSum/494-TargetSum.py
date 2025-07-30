# Last updated: 7/30/2025, 10:44:03 PM
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        
        def bt(index, current_sum):
            if index == len(nums):
                return 1 if current_sum == target else 0
            
            if (index, current_sum) in memo:
                return memo[(index, current_sum)]
            
            addition = bt(index+1, current_sum + nums[index])
            subtract = bt(index+1, current_sum - nums[index])

            memo[(index, current_sum)] = addition +subtract

            return addition + subtract
        
        return bt(0, 0)
