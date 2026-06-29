class Solution(object):
    def isValid(self, s):
        stack = []
        opening = ["(", "{", "["]
        close_to_open = {")":"(", "]":"[", "}":"{"}
        for i in range(len(s)):
            if s[i] in opening:
                stack.append(s[i])
            elif stack and s[i] in close_to_open and stack[-1] == close_to_open[s[i]]:
                stack.pop()
            else:
                return False
        return stack == []

        