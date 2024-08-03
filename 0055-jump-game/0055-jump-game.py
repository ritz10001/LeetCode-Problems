class Solution(object):
    def canJump(self, nums):
        maxJump = 0
        for i in range(len(nums)):
            if i == len(nums) - 1:
                return True
            maxJump = max(nums[i], maxJump)
            if maxJump == 0:
                return False
            maxJump-=1