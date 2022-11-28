class Solution:
    def climbStairs(self, n: int) -> int:
        one_down = two_down = 1
        for i in range(2, n+1):
            one_down, two_down = one_down + two_down, one_down
        return one_down