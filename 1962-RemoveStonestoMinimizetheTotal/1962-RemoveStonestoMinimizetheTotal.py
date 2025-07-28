# Last updated: 7/28/2025, 11:13:24 PM
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        total = sum(piles)
        piles = [-i for i in piles]
        
        heapq.heapify(piles)

        while k > 0:
            temp = heapq.heappop(piles)*-1

            total -= temp//2
            temp -= temp//2
            heapq.heappush(piles, temp*-1)
            k -= 1
            
        return total
            
