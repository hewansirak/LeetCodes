# Last updated: 8/14/2025, 10:37:01 AM
class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        n = len(nums)
        
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                count += 1
        
        return count <= 1