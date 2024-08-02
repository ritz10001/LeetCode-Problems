class Solution(object):
    def strStr(self, haystack, needle):
        n = len(needle)
        h = len(haystack)
        idx = 0
        while idx < h:
            if haystack[idx:idx+n] == needle:
                return idx
            idx += 1
        return -1