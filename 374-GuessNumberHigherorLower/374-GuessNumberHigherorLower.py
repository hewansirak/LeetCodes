# Last updated: 5/5/2025, 9:07:26 PM
class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        r = n
        while True:
            m = (l + r) // 2
            res = guess(m)
           
            if res > 0:
                l = m + 1
            elif res < 0:
                r = m - 1
            else:
                return m
        