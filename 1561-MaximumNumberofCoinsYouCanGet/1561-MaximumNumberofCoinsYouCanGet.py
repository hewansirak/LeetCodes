# Last updated: 9/20/2025, 10:51:44 PM
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        total = 0
        pair = len(piles) // 3
        for i in range(pair, len(piles), 2):
            total += piles[i]
        return total