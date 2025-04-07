# Last updated: 4/7/2025, 7:54:11 PM
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        starts = sorted([(intervals[k][0], k) for k in range(n)])
        ends = sorted([(intervals[k][1], k) for k in range(n)])
        res = [-1] * n
        j = 0  

        for i in range(n):
            end_time, original_end_index = ends[i]
            while j < n and starts[j][0] < end_time:
                j += 1

            if j < n:
                start_time, original_start_index = starts[j]
                res[original_end_index] = original_start_index
        return res