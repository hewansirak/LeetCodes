# Last updated: 9/1/2025, 10:51:22 PM
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = set()
        min_heap = [(0, 0)]
        total = 0

        while len(visited) < n:
            mnh_dis, i = heapq.heappop(min_heap)
            if i in visited:
                continue
            visited.add(i)
            total += mnh_dis
            xi, yi = points[i]

            for j in range(n):
                if j not in visited:
                    xj, yj = points[j]
                    ngh_dis = abs(xi-xj) + abs(yi-yj)
                    heapq.heappush(min_heap, (ngh_dis, j))

        return total