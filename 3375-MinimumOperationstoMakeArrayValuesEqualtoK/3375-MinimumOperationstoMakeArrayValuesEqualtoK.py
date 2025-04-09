# Last updated: 4/9/2025, 8:24:00 AM
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if nums==[k]*len(nums):
            return 0
        s=set()
        for i in nums:
            if i>k and i not in s:
                s.add(i)
        if len(s)!=0 and min(nums)>=k:
            return len(s)
        return -1