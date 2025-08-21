# Last updated: 8/21/2025, 11:42:36 PM
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0

        for n in nums:
            res ^= n
        
        return res