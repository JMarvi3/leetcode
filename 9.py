class Solution:
    def isPalindrome(self, x: int) -> bool:
        def reverse(x: int) -> int:
            result = 0
            while x:
                result = result*10 + x%10
                x //= 10
            return result
        return x >= 0 and reverse(x) == x