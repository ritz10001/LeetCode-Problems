class Solution(object):
    def isPalindrome(self, x):
        str_num = str(x)
        l = 0
        r = len(str_num) - 1
        while l < r:
            if str_num[l] != str_num[r]:
                return False
            l += 1
            r -= 1
        return True
        