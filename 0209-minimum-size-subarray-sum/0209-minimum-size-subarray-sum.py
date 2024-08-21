class Solution(object):
    def minSubArrayLen(self, target, nums):
        minLen = len(nums) + 1
        curr = 0
        l = 0
        for i in range(len(nums)):
            curr += nums[i]
            while curr >= target:
                minLen = min(minLen, i + 1 - l)
                curr -= nums[l]
                l += 1
        if minLen == len(nums) + 1:
            return 0
        return minLen