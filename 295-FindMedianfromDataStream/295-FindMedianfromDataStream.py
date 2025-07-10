# Last updated: 7/10/2025, 10:59:16 PM
class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -1 * num)
        heapq.heappush(self.min_heap, -1 * heapq.heappop(self.max_heap))

        if len(self.min_heap) > len(self.max_heap):
            curr_value = -1 * heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, curr_value)
    
    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            median = (-1 * self.max_heap[0]) + self.min_heap[0]
            return median / 2
        else:
            return -1 * self.max_heap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()