# Last updated: 11/19/2025, 11:52:35 PM
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        s = set(nums)      
        
        while original in s: 
            original *= 2
        
        return original