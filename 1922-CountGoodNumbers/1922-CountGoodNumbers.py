# Last updated: 5/2/2025, 10:09:23 PM
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 1000000007
        odd = n//2
        even = n//2 + n%2
        
        def pow(x,n):
        
            if n==0:
                return 1
            if n%2==0:
                return pow((x*x)%mod, n//2)
            else:
                return x * pow((x*x)%mod, n//2)
        
        return (pow(5,even)%mod * pow(4,odd)%mod)%mod