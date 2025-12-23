class Solution(object):
    def maxArea(self, height):
        maxx = float("-inf")
        l = 0
        r = len(height) - 1
        while l < r:
            currArea = min(height[l], height[r]) * (r - l)
            maxx = max(maxx, currArea)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxx
        