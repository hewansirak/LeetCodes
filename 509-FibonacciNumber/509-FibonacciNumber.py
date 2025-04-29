# Last updated: 4/29/2025, 9:37:29 PM
class Solution:
    def fib(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 0:
            return 0
        return self.fib(n - 1) + self.fib(n - 2)
        