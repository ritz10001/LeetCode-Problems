class Solution(object):
    def maxProfit(self, prices):
        l = 0
        r = 1
        maxProfit = 0
        while r < len(prices):
            maxProfit = max(maxProfit, prices[r] - prices[l])
            if prices[r] < prices[l]:
                l = r
            r += 1
        return maxProfit

        