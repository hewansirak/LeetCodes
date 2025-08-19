# Last updated: 8/19/2025, 10:37:47 PM
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        sub = 1 
        for i in range(1, n + 1):
            if sub * 2 == i: 
                sub = i 
            
            res[i] = res[i - sub] + 1

        return res
           