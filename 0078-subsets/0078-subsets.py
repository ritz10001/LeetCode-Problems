class Solution(object):
    def subsets(self, nums):
        res = []
        sol = []
        def backtrack(i):
            if i >= len(nums):
                res.append(list(sol))
                return
            sol.append(nums[i])
            backtrack(i + 1)
            sol.pop()
            backtrack(i + 1)
        backtrack(0)
        return res

        