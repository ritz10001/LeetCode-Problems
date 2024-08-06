class Solution(object):
    def isSubsequence(self, s, t):
        p = 0
        for i in range(len(t)):
            if p < len(s) and t[i] == s[p]:
                p += 1
        if p == len(s):
            return True
        return False
    