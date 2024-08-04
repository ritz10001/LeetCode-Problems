class Solution(object):
    def productExceptSelf(self, nums):
        prd = [1] * len(nums)
        left_product = 1
        right_product = 1

        for i in range(len(nums)):
            prd[i] = left_product
            left_product *= nums[i]
        
        for i in range(len(nums)-1, -1,-1):
            prd[i] *= right_product
            right_product *= nums[i]
            
        return prd
    
            