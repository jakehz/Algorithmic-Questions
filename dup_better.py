class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        startIndex = 0
        while startIndex < (len(nums) - 1):
            for i in range(startIndex + 1, len(nums)):
                if nums[startIndex] == nums[i]:
                    return True
            startIndex += 1
        return False
                
            