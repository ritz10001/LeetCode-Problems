class Solution(object):
    def minPathSum(self, grid):
        r = len(grid)
        c = len(grid[0])
        dp = [[0 for i in range(c)] for j in range(r)]
        row_sum = 0
        col_sum = 0
        for i in range(c):
            dp[0][i] = grid[0][i] + row_sum
            row_sum += grid[0][i]
        for i in range(r):
            dp[i][0] = grid[i][0] + col_sum
            col_sum += grid[i][0]
        for i in range(1, r):
            for j in range(1, c):
                top = dp[i-1][j]
                left = dp[i][j-1]
                dp[i][j] = min(top + grid[i][j], left + grid[i][j])
        return dp[r-1][c-1]
            