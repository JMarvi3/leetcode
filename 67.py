class Solution:
    def addBinary(self, a: str, b: str) -> str:
        len_a, len_b = len(a), len(b)
        result = []
        c = 0
        for i in range(max(len_a, len_b)):
            if i<len_a:
                c += int(a[-i-1])
            if i<len_b:
                c += int(b[-i-1])
            result.append(str(c%2))
            c//=2
        while c>0:
            result.append(str(c%2))
            c//=2
        return ''.join(reversed(result))