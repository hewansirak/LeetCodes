# Last updated: 10/13/2025, 1:24:56 PM
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        # If first letter matches 
        # dfs search
        # mark visited & explore the 4 directions
        # unmark

        rows = len(board)
        cols = len(board[0])

        def dfs(r, c, i):

            if i == len(word):
                return True
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i]:
                return False           

            temp, board[r][c] = board[r][c], "#"
            found = (dfs(r+1, c, i+1) or 
                    dfs(r-1, c, i+1) or
                    dfs(r, c+1, i+1) or
                    dfs(r, c-1, i+1)
                    )
            board[r][c] = temp
            return found
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True
        return False
            
