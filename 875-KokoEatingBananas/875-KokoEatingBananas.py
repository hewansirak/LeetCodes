# Last updated: 5/9/2025, 11:26:10 PM
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        while low <= high:
            mid = low + (high - low) // 2
            total_hours = sum((pile + mid - 1) // mid for pile in piles)

            if total_hours > h:
                low = mid + 1
            else:
                high = mid - 1

        return low
