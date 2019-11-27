class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Algorithm takes a list with zeroes and other numbers and moves the zeroes to the back
        O(n) time complexity, O(1) storage
        """
        currCopy = 0
        for i in range(0,len(nums)):
            if nums[i] != 0:
                nums[currCopy] = nums[i]
                currCopy += 1
        for i in range(currCopy, len(nums)):
            nums[i] = 0
            