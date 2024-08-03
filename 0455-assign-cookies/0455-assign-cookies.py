class Solution(object):
    def findContentChildren(self, g, s):
        satisfied = 0
        c = 0
        s.sort()
        g.sort()
        while c < len(s):
            if satisfied < len(g) and s[c] >= g[satisfied]:
                satisfied += 1
            elif satisfied >= len(g):
                break
            c += 1
                
        return satisfied
