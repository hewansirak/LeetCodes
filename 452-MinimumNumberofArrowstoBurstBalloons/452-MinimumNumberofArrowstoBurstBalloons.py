# Last updated: 7/18/2025, 9:37:00 PM
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        ans = 1
        end_val = points[0][1]
        for start, end in points[1:]:
            if start <= end_val:
                end_val = min(end_val, end)
            else:
                ans += 1
                end_val = end
        return ans