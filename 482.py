class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '').upper()
        result = [s[max(0, i-k+1): i+1] for i in range(len(s)-1, -1, -k)]
        return '-'.join(reversed(result))