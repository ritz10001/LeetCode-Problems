class Solution(object):
    def longestMountain(self, arr):
        inc = [0] * len(arr)
        dec = [0] * len(arr)
        increasingSeq = 0
        longest = 0
        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]:
                increasingSeq += 1
                inc[i] = increasingSeq
            else:
                increasingSeq = 0
        increasingSeq = 0
        for i in range(len(arr)-2, -1, -1):
            if arr[i] > arr[i+1]:
                increasingSeq += 1
                dec[i] = increasingSeq
            else:
                increasingSeq = 0
        for i in range(len(arr)):
            if inc[i] > 0 and dec[i] > 0:
                longest = max(longest, inc[i] + dec[i] + 1)
        return longest