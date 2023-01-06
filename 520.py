class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        num_caps = sum(c.isupper() for c in word)
        return num_caps == 0 or num_caps == len(word) or (num_caps == 1 and word[0].isupper())