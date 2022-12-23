class Solution:
    def arrangeCoins(self, n: int) -> int:
        # complete staircase = r*(r+1)/2
        # r^2 + r >= 2*n
        # r^2 + r - 2*n >= 0
        # quadratic formula: a=1, b=1, c=-2*n
        # r = (-1 + sqrt(1 + 8*n)) / 2
        return int((sqrt(1 + 8*n) - 1) / 2)
