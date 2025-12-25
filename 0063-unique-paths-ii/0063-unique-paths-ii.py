import copy
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        if obstacleGrid[0][0] == 1:
            return 0
        r = len(obstacleGrid)
        c = len(obstacleGrid[0])
        dp = [[0 for j in range(c)] for i in range(c)]
        if obstacleGrid[0][0] == 0:
            dp[0][0] = 1
        for i in range(r):
            for j in range(c):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                if j > 0:
                    dp[i][j] += dp[i][j-1]
        return dp[r-1][c-1]
                    
            