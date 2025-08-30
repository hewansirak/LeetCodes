# Last updated: 8/30/2025, 9:53:30 PM
class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        mask = 0xffffffff
        
        while (b & mask) > 0:
            
            carry = ( a & b ) << 1
            a = (a ^ b) 
            b = carry
        
        return (a & mask) if b > 0 else a