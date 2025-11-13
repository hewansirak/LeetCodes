# Last updated: 11/13/2025, 10:36:15 PM
class Solution:
    def findNthDigit(self, n: int) -> int:
        length = 1
        count = 9
        start = 1

        # Which digit block
        while n > length * count:
            n -= length * count
            length += 1
            count *= 10
            start *= 10

        num = start + (n - 1) // length

        indx = (n - 1) % length
        return int(str(num)[indx])