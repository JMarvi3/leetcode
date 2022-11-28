class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_of_squares(n):
            res = 0
            while n:
                res += (n%10)**2
                n //= 10
            return res
        seen = {1}
        while n not in seen:
            seen.add(n)
            n = sum_of_squares(n)
        return n == 1
