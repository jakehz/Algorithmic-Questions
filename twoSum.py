"""Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice."""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numInds = {}
        # create a dict of nums and corresp. indices
        for i in range(0,len(nums)):
            numInds[nums[i]] = i
        
        for j,x in enumerate(nums):
            # corresponding value num
            corr = target - x
            # access time of O(1) since dict
            if corr in numInds and j != numInds[corr]:
                    return [j, numInds[corr]]