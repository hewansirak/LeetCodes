# Last updated: 5/31/2025, 11:29:03 PM
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        same = True
        n = 2**(n - 1)

        while n != 1:
            n //= 2

            if k > n:
                k -= n
                same = not same

        return 0 if same else 1