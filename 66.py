class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = list(digits)
        c = 1
        for i in reversed(range(len(res))):
            if c==0:
                break
            num = res[i] + c
            res[i] = num%10
            c = num//10
        return [c] + res if c else res