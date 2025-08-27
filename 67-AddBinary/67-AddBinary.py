# Last updated: 8/27/2025, 11:16:58 PM
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a, 2)
        b = int(b, 2)
        s = a + b
        return bin(s)[2:]
