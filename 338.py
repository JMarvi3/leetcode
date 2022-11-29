class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n+1)
        if n>0:
            res[1] = 1
            for i in range(2, n+1):
                res[i] = i%2 + res[i//2]
        return res