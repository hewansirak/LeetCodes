# Last updated: 11/16/2025, 10:34:45 PM
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.solve(nums, k) - self.solve(nums, k - 1)

    def solve(self, nums, k):
        count = {}
        l = 0
        ans = 0

        for r in range(len(nums)):
            count[nums[r]] = count.get(nums[r], 0) + 1

            # shrink window 
            while len(count) > k:
                count[nums[l]] -= 1
                if count[nums[l]] == 0:
                    del count[nums[l]]
                l += 1

            # no. ending at r
            ans += (r - l + 1)

        return ans