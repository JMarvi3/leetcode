class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = []
        c = 0
        for i in range(max(len(num1), len(num2))):
            if i < len(num1):
                c += int(num1[-i-1])
            if i < len(num2):
                c += int(num2[-i-1])
            result.append(c % 10)
            c //= 10
        while c:
            result.append(c % 10)
            c //= 10
        return ''.join(map(str, reversed(result)))
