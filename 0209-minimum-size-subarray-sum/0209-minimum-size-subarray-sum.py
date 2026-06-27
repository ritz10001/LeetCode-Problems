class Solution(object):
    def minSubArrayLen(self, target, nums):
        l = 0
        res = float("inf")
        currentSum = 0
        for r in range(len(nums)):
            currentSum += nums[r]
            while currentSum >= target:
                res = min(res, r - l + 1)
                currentSum -= nums[l]
                l += 1
        if res == float("inf"):
            return 0
        return res