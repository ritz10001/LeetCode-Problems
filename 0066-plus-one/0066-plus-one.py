from collections import deque
class Solution(object):
    def plusOne(self, digits):
        res = deque([])
        carry = 0
        for i in range(len(digits) - 1, -1, -1):
            if i == len(digits) - 1:
                total = digits[i] + 1 + carry
            else:
                total = digits[i] + carry
            carry = total // 10
            summ = total % 10
            res.appendleft(summ)
        if carry:
            res.appendleft(carry)
        return list(res)
            