# Last updated: 10/11/2025, 1:33:56 PM
class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        num = x
        reverse = 0

        if x < 0:
            return False

        while x > 0:
            last = x % 10
            reverse = (reverse * 10) + last
            x = x // 10


        return num == reverse