class Solution(object):
    def lengthOfLongestSubstring(self, s):
        longest = 0
        l = 0
        chars = set()
        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            longest = max(longest, r - l + 1)
        return longest

        