class Solution(object):
    def summaryRanges(self, nums):
        if len(nums) == 0:
            return []
        res = []
        currRange = 1
        for i in range(1, len(nums)+1):
            if i < len(nums) and nums[i] - nums[i-1] == 1:
                currRange += 1
            else:
                if currRange > 1:
                    string = str(nums[i-currRange]) + "->" + str(nums[i-1])
                    res.append(string)
                else:
                    res.append(str(nums[i-1]))
                currRange = 1
        return res