class Solution(object):
    def longestPalindromeSubseq(self, s):
        s2 = s[::-1]
        length = len(s)
        dp = [[0 for j in range(length+1)] for i in range(length+1)]
        for i in range(length - 1, -1, -1):
            for j in range(length - 1, -1, -1):
                if s[i] == s2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])
        return dp[0][0]
        
        