# Last updated: 10/13/2025, 12:04:33 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        group = set()

        for i in nums:
            if i in group:
                return True
            group.add(i)
        return False