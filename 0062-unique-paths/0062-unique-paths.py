class Solution(object):
    def uniquePaths(self, m, n):
        dp = [[1 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                total = 0
                if i > 0:
                    total += dp[i-1][j]
                if j > 0:
                    total += dp[i][j-1]
                dp[i][j] = max(dp[i][j], total)
        return dp[m-1][n-1]
        