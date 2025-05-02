# Last updated: 5/2/2025, 11:07:16 PM
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        result = 0

        for people in range(1, n + 1):
            result = (result + k) % people
        return result + 1

    def helper(n, k):
        if n == 1:
            return 0
        return (helper(n - 1, k) + k) % n
