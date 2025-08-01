# Last updated: 8/1/2025, 10:51:48 PM
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        dist = [[float('inf')] * n for _ in range(m)]
        queue = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    queue.append((i, j))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            row, col = queue.popleft()

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

                if 0 <= new_row < m and 0 <= new_col < n:
                    if dist[new_row][new_col] > dist[row][col] + 1:
                        dist[new_row][new_col] = dist[row][col] + 1
                        queue.append((new_row, new_col))
        
        return dist