# Last updated: 11/26/2025, 10:53:45 PM
1class Solution:
2    def kthGrammar(self, n: int, k: int) -> int:
3        same = True
4        n = 2**(n - 1)
5
6        while n != 1:
7            n //= 2
8
9            if k > n:
10                k -= n
11                same = not same
12
13        return 0 if same else 1