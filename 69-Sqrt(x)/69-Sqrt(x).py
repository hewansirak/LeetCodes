# Last updated: 12/12/2025, 11:44:16 PM
1class Solution:
2    def mySqrt(self, x: int) -> int:
3        return bisect_right( range(x+1), 0 , key=lambda q: q * q-x ) - 1
4