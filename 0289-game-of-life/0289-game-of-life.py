import copy
class Solution(object):
    def gameOfLife(self, board):
        boardCopy = copy.deepcopy(board)
        offsets = [(0,1),(1,0),(1,1),(-1,-1),(-1,0),(0,-1), (-1,1),(1,-1)]
        r = len(boardCopy)
        c = len(boardCopy[0])
        for i in range(r):
            for j in range(c):
                current_cell = boardCopy[i][j]
                live_neighbors = 0
                for x, y in offsets:
                    offset_x = x + i
                    offset_y = y + j
                    if 0 <= offset_x < r and 0 <= offset_y < c: # live cell
                        live_neighbors += boardCopy[offset_x][offset_y]
                if current_cell == 1:
                    if live_neighbors not in (2,3):
                        board[i][j] = 0 
                else:
                    if live_neighbors == 3:
                        board[i][j] = 1
        