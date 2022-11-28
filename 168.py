class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        a = ord('A')
        result = []
        while columnNumber > 0:
            columnNumber -= 1
            result.append(chr(a + columnNumber % 26))
            columnNumber //= 26
        return ''.join(reversed(result))
