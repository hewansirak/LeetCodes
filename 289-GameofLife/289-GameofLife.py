class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        num_rows = len(board)
        num_cols = len(board[0])

        for i in range(num_rows):
            for j in range(num_cols):
                count = 0

                for m in range(max(0, i - 1), min(i + 2, num_rows)):
                    for n in range(max(0, j - 1), min(j + 2, num_cols)):
                        if m == i and n == j:
                            continue
                        count += board[m][n] & 1

                if count | board[i][j] == 3:
                    board[i][j] |= 2

        for i in range(num_rows):
            for j in range(num_cols):
                board[i][j] >>= 1

        