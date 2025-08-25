# Last updated: 8/25/2025, 9:40:01 PM
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y 
        count = 0 
        while xor: 
            xor &= xor - 1
            count += 1 

        return count