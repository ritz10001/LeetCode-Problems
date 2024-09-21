class Solution(object):
    def topKFrequent(self, nums, k):
        freq = {}
        res = []
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        res = [i[0] for i in sorted_freq[:k]]
        return res
            