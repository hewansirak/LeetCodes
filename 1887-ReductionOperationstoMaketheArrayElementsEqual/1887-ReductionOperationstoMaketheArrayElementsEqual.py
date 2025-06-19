# Last updated: 6/19/2025, 8:17:50 PM
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()  
        n = len(nums)
        sum_val = 0
        temp = 0

        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                temp += 1  
            sum_val += temp  
        return sum_val