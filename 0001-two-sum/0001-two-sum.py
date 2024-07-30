class Solution(object):
    def twoSum(self, nums, target):
        indices = []
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] in hashmap:
                return [hashmap[nums[i]], i]
            hashmap[target - nums[i]] = i
