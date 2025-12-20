# Last updated: 12/20/2025, 10:14:43 PM
1class Solution:
2    def summaryRanges(self, nums: List[int]) -> List[str]:
3        ans = []
4
5        i = 0
6        while i < len(nums):
7            begin = nums[i]
8            while i < len(nums) - 1 and nums[i] == nums[i + 1] - 1:
9                i += 1
10            end = nums[i]
11            if begin == end:
12                ans.append(str(begin))
13            else:
14                ans.append(str(begin) + "->" + str(end))
15            i += 1
16
17        return ans