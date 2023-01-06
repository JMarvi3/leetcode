class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        b, a = 0, 1
        for _ in range(n - 1):
            b, a = a, a + b
        return a
