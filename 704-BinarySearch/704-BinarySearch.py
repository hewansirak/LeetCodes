# Last updated: 5/7/2025, 10:47:48 PM
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = -1
        high = len(nums)

        while high > low + 1:
            mid = low + (high - low) // 2

            if nums[mid] < target:
                low = mid
            else:
                high = mid

        if high < len(nums) and nums[high] == target:
            return high
        return -1

        