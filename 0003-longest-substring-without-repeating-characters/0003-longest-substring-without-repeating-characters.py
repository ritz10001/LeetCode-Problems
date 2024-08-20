class Solution(object):
    def lengthOfLongestSubstring(self, s):
        maxLen = 0
        charSet = set()
        l = 0
        for i in range(len(s)):
            while s[i] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[i])
            maxLen = max(maxLen, (i + 1) - l)
        return maxLen