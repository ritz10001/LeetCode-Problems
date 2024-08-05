class Solution(object):
    def maxProduct(self, nums):
        global_max = max(nums)
        cur_min, cur_max = 1, 1
        for i in range(len(nums)):
            if nums[i] != 0:
                temp_max = nums[i] * cur_max
                cur_max = max(nums[i], nums[i] * cur_max, nums[i] * cur_min)
                cur_min = min(nums[i], temp_max, nums[i] * cur_min)
                global_max = max(cur_max, global_max)
            else:
                cur_max, cur_min = 1, 1
        return global_max

        