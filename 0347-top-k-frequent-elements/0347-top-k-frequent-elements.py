class Solution(object):
    def topKFrequent(self, nums, k):
        freq = {}
        res = []
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        sortlist = []
        x = list(freq.items())
        print(x)
        for i in range(len(x)):
            max_idx = i
            for j in range(i+1, len(x)):
                if x[j][1] > x[max_idx][1]:
                    max_idx = j
            x[i], x[max_idx] = x[max_idx], x[i]
        for i in range(k):
            res.append(x[i][0])
        return res
            