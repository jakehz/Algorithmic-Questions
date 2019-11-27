# brute force soln
# O(n^2) time complexity
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(0, len(nums)):
            for j in range(0,len(nums)):
                if i != j and nums[i] == nums[j]:
                    return True
        return False