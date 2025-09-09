# Last updated: 9/9/2025, 11:34:39 PM
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
    
        prime = [0] * n  
        for i in range(2, int(n**0.5) + 1):
            if prime[i] == 0:
                for j in range(i * i, n, i): 
                    prime[j] = 1

        return sum(1 for i in range(2, n) if prime[i] == 0)