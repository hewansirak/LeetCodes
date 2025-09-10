# Last updated: 9/10/2025, 11:40:36 PM
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        return gcd(min(nums), max(nums))
