# Last updated: 8/21/2025, 10:16:00 PM
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for i in range(32):
            bsum = 0
            for num in nums:
                bsum += (num >> i) & 1
            if bsum % 3:
                result |= (1 << i)
        if result >= 2**31:
            result -= 2**32
        return result