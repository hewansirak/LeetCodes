# Last updated: 5/7/2025, 11:06:20 PM
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def canCarry(capacity):
            currCapacity = capacity
            curr_ships = 1
            for w in weights:
                if currCapacity - w < 0:
                    curr_ships += 1
                    currCapacity = capacity
                currCapacity -= w
            return curr_ships <= days

        left = max(weights)
        right = sum(weights)
        max_cap = right 

        while left <= right:
            mid = left + (right - left) // 2
            if canCarry(mid):
                max_cap = mid 
                right = mid - 1
            else:
                left = mid + 1

        return max_cap