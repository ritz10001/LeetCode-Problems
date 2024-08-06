class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()
        visited = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i + 1, len(nums) - 1 
            fixed = nums[i]
            while left < right:
                if left > i + 1 and nums[left] == nums[left-1]:
                    left += 1
                    continue
                if right < len(nums) - 1 and nums[right] == nums[right+1]:
                    right -= 1
                    continue
                if fixed + nums[left] + nums[right] < 0:
                    left += 1
                elif fixed + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
        return res
            