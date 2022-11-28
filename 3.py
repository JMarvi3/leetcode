class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = dict()
        start = max_length = 0
        for end, c in enumerate(s):
            if seen.get(c, -1) >= start:
                start = seen[c] + 1
            seen[c] = end
            max_length= max(max_length, end - start + 1)
        return max_length