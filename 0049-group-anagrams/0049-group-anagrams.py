from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        res = defaultdict(list)
        for i in strs:
            count = [0] * 26
            for char in i:
                count[ord(char) - ord("a")] += 1
            res[tuple(count)] += (i, )
        return list(res.values())
        