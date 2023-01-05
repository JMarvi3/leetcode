class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        x = abs(num)
        result = ''
        while x:
            result += str(x % 7)
            x //= 7
        if num < 0:
            result += '-'
        return result[::-1]
