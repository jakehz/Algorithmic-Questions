# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        nums = []
        def helper(node, nums):
            if node != None:
                helper(node.left, nums)
                nums.append(node.val)
                helper(node.right, nums)
        helper(root, nums)
        for i in range(1, len(nums)):
            if nums[i-1] >= nums[i]:
                return False
        return True

        