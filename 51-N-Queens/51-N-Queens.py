# Last updated: 6/24/2025, 11:53:18 PM
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []  
        board = [['.' for _ in range(n)] for _ in range(n)]  

        def is_safe(row, col):
            for r in range(row):
                if board[r][col] == 'Q':
                    return False

            r, c = row - 1, col - 1
            while r >= 0 and c >= 0:
                if board[r][c] == 'Q':
                    return False
                r -= 1
                c -= 1

            r, c = row - 1, col + 1
            while r >= 0 and c < n:
                if board[r][c] == 'Q':
                    return False
                r -= 1
                c += 1

            return True 

        def backtrack(row):
            if row == n:
                solution = [''.join(r) for r in board]
                result.append(solution)
                return

            for col in range(n):
                if is_safe(row, col):
                    board[row][col] = 'Q' 
                    backtrack(row + 1)     
                    board[row][col] = '.'  

        backtrack(0)  
        return result
