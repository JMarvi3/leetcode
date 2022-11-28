class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for i, num in enumerate(nums):
            if num != nums[k]:
                k += 1
                nums[k] = num
        return k+1