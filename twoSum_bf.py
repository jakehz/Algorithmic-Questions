class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            if ((target - nums[i]) in nums):
                index2 = nums.index(target - nums[i])
                if index2 != i:
                    return [i, index2]
