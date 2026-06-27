import copy
class Solution(object):
    def gameOfLife(self, board):
        offsets = [(0,1),(1,0),(1,1),(-1,-1),(-1,0),(0,-1), (-1,1),(1,-1)]
        r = len(board)
        c = len(board[0])
        for i in range(r):
            for j in range(c):
                current_cell = board[i][j]
                live_neighbors = 0
                for x, y in offsets:
                    offset_x = x + i
                    offset_y = y + j
                    if 0 <= offset_x < r and 0 <= offset_y < c: # live cell
                        if board[offset_x][offset_y] in (1,2):
                            live_neighbors += 1
                if current_cell == 1:
                    if live_neighbors not in (2,3): 
                        board[i][j] = 2 # live to dead
                else:
                    if live_neighbors == 3:
                        board[i][j] = 3 # dead to live
        for i in range(r):
            for j in range(c):
                board[i][j] %= 2
        