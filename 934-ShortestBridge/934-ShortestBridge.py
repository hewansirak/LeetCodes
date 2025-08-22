# Last updated: 8/22/2025, 11:52:04 PM
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:

        n = len(grid)
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        
        # Find island first
        def dfs(i, j, q):
            if i < 0 or j < 0 or i >= n or j >= n or grid[i][j] != 1:
                return
            grid[i][j] = 2  # visited 
            q.append((i, j))
            for di, dj in directions:
                dfs(i + di, j + dj, q)
        
        q = deque()
        found = False

        # BFS

        for i in range(n):
            if found:
                break
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j, q)
                    found = True
                    break
        
        steps = 0
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n:
                        if grid[nx][ny] == 1: 
                            return steps
                        if grid[nx][ny] == 0:  
                            grid[nx][ny] = 2
                            q.append((nx, ny))
            steps += 1
