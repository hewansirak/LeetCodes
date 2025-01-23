class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()

        result = float('inf')

        for i in range(len(nums) - k + 1):
            current = nums[i + k - 1] - nums[i]

            if current < result:
                result = current

        return result
            