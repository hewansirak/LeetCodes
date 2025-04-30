# Last updated: 4/30/2025, 10:24:46 PM
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def recurse(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            result = recurse(x * x, n // 2)
            return x * result if n % 2 else result

        result = recurse(x, abs(n))
        return result if n >= 0 else 1 / result
        