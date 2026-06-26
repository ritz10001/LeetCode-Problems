class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)
        nums.reverse()
        # reverse first half
        l = 0
        r = k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        # reverse second half
        l = k
        r = len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        