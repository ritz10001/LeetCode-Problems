class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums)==1:
            return 1
        L, R = 1, 1
        while nums:
            if nums[R] != nums[R-1]:
                nums[L] = nums[R]
                L+=1
            R+=1
            if(R == len(nums)):
                return L
                

        