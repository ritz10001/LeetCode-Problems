class Solution(object):
    def hIndex(self, citations):
        citations.sort()
        h = 0
        n = len(citations)
        for i in range(n):
            if n - i >= citations[i]:
                h = max(h, citations[i])
            else:
                h = max(h, n - i)
        return h
        