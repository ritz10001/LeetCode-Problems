class Solution(object):
    def dailyTemperatures(self, temperatures):
        res = [0 for i in range(len(temperatures))]
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)
        return res

        