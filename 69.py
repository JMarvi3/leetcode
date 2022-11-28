class Solution:
    def mySqrt(self, x: int) -> int:
        # Newton's method
        n = x+1
        while n*n > x:
            n = (n + x//n) // 2
        return n