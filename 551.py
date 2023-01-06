class Solution:
    def checkRecord(self, s: str) -> bool:
        max_late_streak = late_streak = absent = 0
        prev = ''
        for c in s:
            if c == 'A':
                absent += 1
                late_streak = 0
            elif c == 'L':
                late_streak += 1
                max_late_streak = max(max_late_streak, late_streak)
            else: # P
                late_streak = 0
        return absent < 2 and max_late_streak < 3