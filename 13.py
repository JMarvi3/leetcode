class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        result = last_val = d[s[0]]
        for symbol in s[1:]:
            val = d[symbol]
            if val > last_val:
                result -= 2*last_val  # once for the prior addition and once because it is subtraction
            result += val
            last_val = val
        return result