class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {num: i for i, num in enumerate(nums)}
        for i, num in enumerate(nums):
            rem = target - num
            if rem in d and d[rem] != i:
                return [i, d[rem]]