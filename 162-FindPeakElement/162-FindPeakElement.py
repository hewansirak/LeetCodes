# Last updated: 5/20/2025, 4:59:13 PM
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            condition1 = (i == 0) or (nums[i-1] < nums[i])

            condition2 = (i == n - 1) or (nums[i] > nums[i+1])

            if condition1 and condition2:
                return i

        return -1
