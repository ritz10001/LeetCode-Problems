class Solution(object):
    def addBinary(self, a, b):
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        res = ""
        while i >= 0 or j >= 0 or carry:
            val1 = int(a[i]) if i >= 0 else 0
            val2 = int(b[j]) if j >= 0 else 0
            total = (val1 + val2 + carry)
            res += str(total % 2)
            carry = total // 2
            i -= 1
            j -= 1
        return res[::-1]
        
        