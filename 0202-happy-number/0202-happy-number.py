class Solution(object):
    def isHappy(self, n):
        numbers = set()
        while n != 1 and n not in numbers:
            numbers.add(n)
            sumx = 0
            while n > 0:
                sumx += (n % 10) ** 2
                n //= 10
            n = sumx
        return n == 1