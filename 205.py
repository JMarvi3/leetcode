class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        forward, reverse = {}, {}
        for c1, c2 in zip(s, t):
            if forward.get(c1, c2) != c2 or reverse.get(c2, c1) != c1:
                return False
            forward[c1] = c2
            reverse[c2] = c1
        return True