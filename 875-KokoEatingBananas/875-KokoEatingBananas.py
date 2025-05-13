# Last updated: 5/13/2025, 4:13:51 PM
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans = 0

        while low <= high:
            mid = low + (high - low) // 2

            total_hours = sum(math.ceil(pile / mid) for pile in piles)

            if total_hours <= h:
                ans = mid
                high = mid - 1
            else: 
                low = mid + 1
            
        return ans

        
            
