class Solution(object):
    def containsDuplicate(self, nums):
        hmap = {}
        for i in nums:
            if (i in hmap) and (hmap[i]==0):
                return True
            else:
                hmap[i] = 0 
        return False