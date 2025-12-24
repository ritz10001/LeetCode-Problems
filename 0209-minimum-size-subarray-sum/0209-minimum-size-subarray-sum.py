class Solution(object):
    """
    idea: sliding window. Keep a L and R pointer. Start with L, R = 0, 0
    if the sum of a specific window is less than target, increase R. If its
    greater or equal, set the currentMin count accordingly. If otherwise,
    increase L.
    [2,3,1,2,4,2] -> 2 + 3 + 1 + 2 = 8 -> [L:R+1]
     ^     ^
     L     R
    [2,3,1,2,4,2] -> 3 + 1 + 2 + 4 = 10
       ^     ^
    """
    def minSubArrayLen(self, target, nums):
        currentSum = 0
        l = 0
        minLen = float("inf")
        for r in range(len(nums)):
            currentSum += nums[r]
            while currentSum >= target:
                minLen = min(minLen, r-l+1)
                currentSum -= nums[l]
                l += 1
        return minLen if minLen < float("inf") else 0