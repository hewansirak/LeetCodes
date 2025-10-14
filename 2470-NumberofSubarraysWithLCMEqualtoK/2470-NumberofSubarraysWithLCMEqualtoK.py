# Last updated: 10/14/2025, 10:41:24 PM
class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            l = nums[i]
            if l == k:
                count += 1
            for j in range(i + 1, len(nums)):
                l = (l * nums[j]) // gcd(l, nums[j])
                if l == k:
                    count += 1
                elif l > k:
                    break
        return count