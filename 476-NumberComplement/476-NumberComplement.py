# Last updated: 8/19/2025, 10:45:09 PM
class Solution:
    def findComplement(self, num: int) -> int:
        if num == 1:
            return 0

        mask = 1
        while mask <= num:
            mask <<= 1

        mask -= 1

        return num ^ mask

        