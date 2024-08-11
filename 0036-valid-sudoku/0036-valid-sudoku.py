class Solution(object):
    def isValidSudoku(self, board):
        for i in range(len(board)):
            visited = []
            for j in range(len(board)):
                if board[i][j] != "." and board[i][j] in visited:
                    return False
                visited.append(board[i][j])
        for i in range(len(board)):
            visited = []
            for j in range(len(board)):
                if board[j][i] != "." and board[j][i] in visited:
                    return False
                visited.append(board[j][i])
        hashmap = {0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]}
        for i in range(len(board)):
            for j in range(len(board)):
                grid_idx = (i//3) * 3 + j//3
                if board[i][j] != "." and board[i][j] in hashmap[grid_idx]:
                    return False
                hashmap[grid_idx].append(board[i][j])
        return True