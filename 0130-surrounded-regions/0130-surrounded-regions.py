from collections import deque
class Solution(object):
    def solve(self, board):
        rows = len(board)
        cols = len(board[0])

        def dfs(r, c):
            if (r >= rows or r < 0 or c >= cols or c < 0) or board[r][c] != "O":
                return
            board[r][c] = "T"
            dfs(r, c + 1)
            dfs(r, c - 1)
            dfs(r + 1, c)
            dfs(r - 1, c)
        for r in range(rows):
            for c in range(cols):
                if (r == 0 or c == 0 or r == rows - 1 or c == cols - 1) and board[r][c] == "O":
                    dfs(r, c)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"

            

        # TOP
        

