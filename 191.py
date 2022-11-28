class Solution:
    def hammingWeight(self, n: int) -> int:
        def naive_count(n):
            count = 0
            while n:
                if n%2 == 1:
                    count += 1
                n //= 2
            return count
        # counts = dict()
        # for i in range(16):
        #     counts[i] = naive_count(i)
        # count = 0
        # while n:
        #     count += counts[n%16]
        #     n //= 16
        # return count
        return naive_count(n)