class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []
        res = []
        hashmap = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        def dfs(index, path):
            if index == len(digits):
                res.append("".join(path))
                return
            for l in hashmap[digits[index]]:
                path.append(l)
                dfs(index + 1, path)
                path.pop()
        dfs(0, [])
        return res
        