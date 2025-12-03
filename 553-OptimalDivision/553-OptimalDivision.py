# Last updated: 12/3/2025, 10:34:08 PM
1class Solution:
2    def optimalDivision(self, nums: List[int]) -> str:
3        if len(nums) == 1:
4            return str(nums[0])
5        elif len(nums) == 2:
6            return str(nums[0]) + '/' + str(nums[1])
7        else:
8            nums_str = list(map(str, nums))
9            return str(nums[0]) + '/(' + '/'.join(nums_str[1:]) + ')'