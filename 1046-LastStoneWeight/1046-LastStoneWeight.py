# Last updated: 7/11/2025, 10:53:59 PM
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)

        while len(stones) > 1:
            heaviest = -heapq.heappop(stones)
            second_heaviest = -heapq.heappop(stones)

            if heaviest != second_heaviest:
                new = heaviest - second_heaviest
                heapq.heappush(stones, -new)

        if stones:
            return -stones[0]
        else:
            return 0