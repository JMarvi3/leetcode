class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # return n > 0 and (2**30 % n == 0)
        return n > 0 and (n & (n-1) == 0)
