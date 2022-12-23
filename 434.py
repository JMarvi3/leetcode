class Solution:
    def countSegments(self, s: str) -> int:
        # return len(s.split())
        count = 0
        in_segment = False
        for c in s:
            if c == ' ':
                if in_segment:
                    count += 1
                    in_segment = False
            else:
                in_segment = True
        return count + in_segment
