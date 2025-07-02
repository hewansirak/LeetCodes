# Last updated: 7/2/2025, 11:52:35 PM
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        unit_vector = {
            1: [(0, 1), (0, -1)],
            2: [(1, 0), (-1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)]
        }

        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        def dfs(row, col):
            if row == len(grid) - 1 and col == len(grid[0]) - 1:
                return True

            visited[row][col] = 1

            for dx, dy in unit_vector[grid[row][col]]:
                crow, ccol = row + dx, col + dy
                if inbound(crow, ccol) and not visited[crow][ccol] and (-1 * dx, -1 * dy) in unit_vector[grid[crow][ccol]]:
                    found = dfs(crow, ccol)
                    if found:
                        return True
            return False

        r1, c1 = len(grid), len(grid[0])
        visited = [[0] * c1 for _ in range(r1)]
        return dfs(0, 0)
        