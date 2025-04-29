# Last updated: 4/29/2025, 9:24:09 PM
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        if n < 1:
            return False
        
        power = self.isPowerOfFour(n / 4)

        return power

        