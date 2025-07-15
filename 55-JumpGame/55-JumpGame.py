# Last updated: 7/15/2025, 10:33:13 PM
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dist = 0
    
        for n in nums:
            if dist < 0:
                return False
            elif n > dist:
                dist = n
            dist -= 1
        
        return True
            