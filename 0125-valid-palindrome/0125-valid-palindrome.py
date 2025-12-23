class Solution(object):
    """idea
    use l and r pointers and check if lowered (both) equal each other. If 
    either is nonalphanumeric (using !s.isalnum()) then skip that check and
    increment accordingly.
    """
    def isPalindrome(self, s):
        l = 0
        r = len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if l < r:
                if s[l].lower() != s[r].lower():
                    return False
                l += 1
                r -= 1
            
        return True


            