class Solution(object):
    def merge(self, intervals):
        if not intervals:
            return []
        intervals.sort()
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= res[-1][1]: # mergeable
                res[-1] = [min(res[-1][0], intervals[i][0]), max(res[-1][1], intervals[i][1])]
            else:
                res.append(intervals[i])
        return res
        