class Solution(object):
    def coinChange(self, coins, amount):
        coins.sort()
        result = [float('inf')] * (amount + 1)
        result[0] = 0
        for i in range(1, len(result)):
            for j in coins:
                if i - j >= 0:
                    result[i] = min(1 + result[i - j], result[i])
                else:
                    continue
        if result[amount] != float('inf'):
            return result[amount]
        else:
            return -1
        