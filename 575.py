class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        types_of_candies = len(set(candyType))
        num = len(candyType) // 2
        return min(num, types_of_candies)