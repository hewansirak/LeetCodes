# Last updated: 10/19/2025, 11:48:07 PM
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        def fn(x):
            ans = 0
            while x > 1: 
                if x&1: 
                    x = 3*x + 1
                else: 
                    x //= 2
                ans += 1
            return ans 
        
        return sorted(range(lo, hi+1), key=fn)[k-1]