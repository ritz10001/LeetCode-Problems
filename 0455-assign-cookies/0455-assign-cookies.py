class Solution(object):
    def findContentChildren(self, g, s):
        satisfied = 0
        s.sort()
        g.sort()
        for c in range(len(s)):
            if satisfied < len(g) and s[c] >= g[satisfied]:
                satisfied += 1
            elif satisfied >= len(g):
                break
                
        return satisfied
