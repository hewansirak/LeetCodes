# Last updated: 9/8/2025, 11:33:00 PM
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        val = first = second = 0
        for num in nums:
            val ^= num
        val &= -val
        for num in nums:
            if num & val: second ^= num
            else: first ^= num
        return [first, second]