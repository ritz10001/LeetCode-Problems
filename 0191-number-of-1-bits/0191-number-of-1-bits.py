class Solution(object):
    def hammingWeight(self, n):
        counter = 0
        while n > 0:
            n = n & (n-1)
            counter += 1
        return counter

        