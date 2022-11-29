class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        res = 0
        odd_used = False
        for c, n in count.items():
            if not odd_used and n % 2:
                res += n
                odd_used = True
            else:
                res += n - n % 2
        return res
