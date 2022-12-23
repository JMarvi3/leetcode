class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # I needed help with this one.
        for num in nums:
            i = abs(num) - 1
            nums[i] = -abs(nums[i])
        return [i+1 for i, v in enumerate(nums) if v > 0]
