# Last updated: 12/11/2025, 10:41:06 PM
1class Solution:
2    def jump(self, nums: List[int]) -> int:
3        jumps, max_reach, steps = 0, 0, 0
4
5        for i in range(len(nums)-1):
6            max_reach = max(max_reach, i + nums[i])
7            if i == steps:
8                jumps += 1
9                steps = max_reach
10        return jumps