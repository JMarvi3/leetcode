from collections import deque
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = deque()
        nums1_dict = {v: i for i, v in enumerate(nums1)}
        result = [-1]*len(nums1)
        for i, num in enumerate(nums2):
            while stack and stack[-1] < num:
                result[nums1_dict[stack.pop()]] = num
            if num in nums1_dict:
                stack.append(num)
        return result