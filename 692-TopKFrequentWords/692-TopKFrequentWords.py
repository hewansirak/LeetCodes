# Last updated: 9/27/2025, 12:09:02 AM
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words_map = Counter(words)
        heap = []
        res = []
        for num in words_map:
            heapq.heappush(heap, (-1*words_map[num], num))
        for _ in range(k):
            if not heap:
                break
            res.append(heapq.heappop(heap)[1])
        return res
       