class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        tank = 0
        res = 0
        if sum(gas) < sum(cost):
            return -1
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                tank = 0
                res = i + 1
        return res


            