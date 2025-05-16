# Last updated: 5/16/2025, 9:25:06 PM
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)

        if m * k > n:
            return -1

        def can_make_bouquets(day: int) -> bool:
            bouquets = 0
            adjacent_flowers = 0
            for d in bloomDay:
                if d <= day:
                    adjacent_flowers += 1
                    if adjacent_flowers == k:
                        bouquets += 1
                        adjacent_flowers = 0
                else:
                    adjacent_flowers = 0
                if bouquets >= m:
                    return True
            return bouquets >= m

        left, right = min(bloomDay), max(bloomDay)
        minimum_days = -1

        while left <= right:
            mid = (left + right) // 2
            if can_make_bouquets(mid):
                minimum_days = mid
                right = mid - 1  
            else:
                left = mid + 1 

        return minimum_days