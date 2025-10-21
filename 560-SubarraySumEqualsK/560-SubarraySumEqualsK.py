# Last updated: 10/21/2025, 11:58:19 PM
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        count = 0
        current = 0
        prefixSum = {0:1}

        for n in nums:
            count += n
            if count - k in prefixSum:
                current += prefixSum[count - k]
            prefixSum[count] = prefixSum.get(count, 0) + 1

        return current
