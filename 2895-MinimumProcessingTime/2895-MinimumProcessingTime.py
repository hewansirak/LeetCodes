# Last updated: 3/24/2025, 10:31:05 PM
class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        return max(a+b for a,b in zip(sorted(processorTime*4),sorted(tasks)[::-1]))

        