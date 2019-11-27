from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(0, k):
            temp = nums[len(nums) - 1]
            del nums[len(nums) - 1]
            nums.insert(0, temp))