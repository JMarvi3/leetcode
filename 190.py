class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            result = result*2 + n%2
            n //= 2
        return result