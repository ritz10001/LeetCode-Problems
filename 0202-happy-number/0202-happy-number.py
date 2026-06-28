class Solution(object):
    def isHappy(self, n):
        numbers = set()
        while n not in numbers:
            numbers.add(n)
            sumx = 0
            while n > 0:
                digit = n % 10
                sumx += digit ** 2
                n //= 10
            if sumx == 1:
                return True
            n = sumx
        return False