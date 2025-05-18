# Last updated: 5/18/2025, 8:44:56 PM
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans = 0
        l = 0
        product = 1

        for r, num in enumerate(nums):
            product *=num
            while product >= k and l <= r:
                product //= nums[l]
                l += 1
            ans += r - l + 1
        return ans