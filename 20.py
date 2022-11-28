class Solution:
    def isValid(self, s: str) -> bool:
        matches = dict([')(', '}{', ']['])
        stack = deque()
        for c in s:
            if c in matches:
                if not stack or stack.pop() != matches[c]:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0