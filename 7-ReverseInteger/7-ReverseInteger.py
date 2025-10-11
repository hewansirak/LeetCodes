# Last updated: 10/11/2025, 1:11:45 PM
class Solution:
    def reverse(self, x: int) -> int:
        
        reverse = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x != 0:

            if  reverse > (2**31 - 1) //10 :
                return 0
        
            last = x % 10
            reverse = (reverse * 10 ) + last
            x = x // 10
            
        return sign * reverse
            
