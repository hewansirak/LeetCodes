# Last updated: 7/17/2025, 11:00:06 PM
class Solution:
    def minPatches(self, nums: list[int], target: int) -> int:
        last_num = 1
        count = 0
        index = 0

        while target >= last_num:
            if index < len(nums) and nums[index] <= last_num:
                last_num += nums[index]
                index += 1
            else:
                last_num += last_num
                count += 1
        return count