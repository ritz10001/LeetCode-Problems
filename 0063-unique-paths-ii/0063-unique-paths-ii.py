import copy
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        if obstacleGrid[0][0] == 1:
            return 0
        r = len(obstacleGrid)
        c = len(obstacleGrid[0])
        dp = copy.deepcopy(obstacleGrid)
        for i in range(c):
            if dp[0][i] == 1:
                dp[0][i] = "0"
                break
            dp[0][i] = "1"
        for i in range(r):
            if dp[i][0] == 1:
                dp[i][0] = "0"
                break
            dp[i][0] = "1"
        for i in range(r):
            for j in range(c):
                if dp[i][j] == 1:
                    dp[i][j] = "0"
                    continue
                if dp[i][j] == "0":
                    continue
                total = 0
                if i > 0:
                    total += int(dp[i-1][j])
                if j > 0:
                    total += int(dp[i][j-1])
                dp[i][j] = max(int(dp[i][j]), total)
        return int(dp[r-1][c-1])
            
            