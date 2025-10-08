# Last updated: 10/8/2025, 11:46:22 PM
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        health -= grid[0][0] + grid[-1][-1]
        if health < 1:
            return False
        
        m = len(grid)
        n = len(grid[0])
        grid[0][0] = grid[-1][-1] = 0

        h = [(-health, 0, 0)]
        healths = {(0, 0): -health}

        while h:
            current_health, x, y = heapq.heappop(h)
            if current_health > healths[(x, y)]:
                continue
            for u, v in ((x - 1, y), (x, y - 1),
                         (x + 1, y), (x, y + 1)):
                if (0 <= u < m and 0 <= v < n):
                    next_health = current_health + grid[u][v]
                    if next_health == 0:
                        continue
                    if u == m - 1 and v == n - 1:
                        return True
                    if next_health < healths.get((u, v), 0):
                        healths[(u, v)] = next_health
                        heapq.heappush(h, (next_health, u, v))

        return False