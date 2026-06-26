class Solution(object):
    def jump(self, nums):
        l = 0
        r = 0
        maxJump = 0
        res = 0
        while r < len(nums) - 1:
            for i in range(l, r + 1):
                maxJump = max(maxJump, i + nums[i])
            l = r + 1
            r = maxJump
            res += 1
        return res