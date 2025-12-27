class Solution(object):
    def gameOfLife(self, board):
        offsets = [(-1,-1),(-1,0),(-1,1),(0,-1),
                (0,1),(1,-1),(1,0), (1,1)]
        rows = len(board)
        cols = len(board[0])
        def mark_cell(r,c):
            live = 0
            dead = 0
            for (i, j) in offsets:
                rx = i + r
                cy = j + c
                if 0 <= rx < rows and 0 <= cy < cols:
                    if boardcopy[rx][cy] == 1:
                        live += 1
                    else:
                        dead += 1
            if boardcopy[r][c] == 1 and live < 2:
                board[r][c] = 0 #mark as dead
            elif boardcopy[r][c] == 1 and 2 <= live <= 3:
                board[r][c] = 1
            elif boardcopy[r][c] == 1 and live > 3:
                board[r][c] = 0
            elif boardcopy[r][c] == 0 and live == 3:
                board[r][c] = 1
                
        boardcopy = copy.deepcopy(board)
        for r in range(rows):
            for c in range(cols):
                mark_cell(r,c)
            