# Last updated: 7/8/2025, 11:54:45 PM
class Solution:
    def solve(self, board: List[List[str]]) -> None:

        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])

        def dfs(r, c):
            if 0 <= r < m and 0 <= c < n and board[r][c] == 'O':
                board[r][c] = '#'  
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)

        for c in range(n):
            if board[0][c] == 'O':
                dfs(0, c)
            if board[m - 1][c] == 'O':
                dfs(m - 1, c)

        for r in range(m):
            if board[r][0] == 'O':
                dfs(r, 0)
            if board[r][n - 1] == 'O':
                dfs(r, n - 1)

        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O':
                    board[r][c] = 'X'  
                elif board[r][c] == '#':
                    board[r][c] = 'O'  