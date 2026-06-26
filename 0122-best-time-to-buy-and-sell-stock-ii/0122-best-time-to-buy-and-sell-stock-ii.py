class Solution(object):
    def maxProfit(self, prices):
        maxP = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                maxP += prices[i] - prices[i-1]
        return maxP 
                
        