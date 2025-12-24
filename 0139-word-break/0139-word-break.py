class Solution(object):
    def wordBreak(self, s, wordDict):
        maxLen = len(max(wordDict, key = len)) 
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for char in range(1, len(s) + 1):
            for i in range(char - 1, char - maxLen - 1, -1):
                if i < 0:
                    break
                if s[i: char] in wordDict and dp[i]:
                    dp[char] = True
                    break
        return dp[len(s)]