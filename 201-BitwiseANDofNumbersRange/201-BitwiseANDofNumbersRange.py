# Last updated: 8/28/2025, 12:51:27 AM
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        i = 0

        while left != right:
            left >>= 1
            right >>= 1
            i +=1
        return left << i
        