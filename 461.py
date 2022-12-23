class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        distance = 0
        while x or y:
            if x%2 != y%2:
                distance += 1
            x //= 2
            y //= 2
        return distance
