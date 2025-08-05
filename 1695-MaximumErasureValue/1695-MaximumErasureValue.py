# Last updated: 8/5/2025, 8:06:21 AM
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        prefix = [0]
        n = len(nums)

        for num in nums:
            prefix.append(prefix[-1] + num)

        mpp = {}
        ans = 0
        prev = 0
        
        for i in range(n):
            if nums[i] in mpp:
                prev = max(prev, mpp[nums[i]] + 1)
            
            mpp[nums[i]] = i
            ans = max(ans, prefix[i + 1] - prefix[prev])
            
        return ans
        