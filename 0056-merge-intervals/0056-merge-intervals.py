class Solution(object):
    def merge(self, intervals):
        if not intervals:
            return []
        intervals.sort()
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            start1 = res[-1][0]
            start2 = intervals[i][0]
            end1 = res[-1][1]
            end2 = intervals[i][1]
            if start2 <= end1: # mergeable
                merged_start = min(start1, start2)
                merged_end = max(end1, end2)
                merged_interval = [merged_start, merged_end]
                res[-1] = merged_interval
            else:
                res.append(intervals[i])
        return res
        