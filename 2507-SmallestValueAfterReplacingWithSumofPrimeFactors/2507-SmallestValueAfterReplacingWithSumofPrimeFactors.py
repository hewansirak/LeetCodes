# Last updated: 9/21/2025, 7:31:40 PM
class Solution:
    def smallestValue(self, n: int) -> int:
        prev = n
        ans = 0

        while not n % 2:                 
                ans += 2
                n //= 2

        for i in range(3, n+1, 2):       
                while not n % i:
                    ans += i
                    n //= i

        return self.smallestValue(ans) if ans != prev else ans