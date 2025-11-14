# Last updated: 11/14/2025, 11:15:47 PM
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        result = 0

        for people in range(1, n + 1):
            result = (result + k) % people
        return result + 1

        def solve(n, k):
            if n == 1:
                return 0
            return (solve(n - 1, k) + k) % n