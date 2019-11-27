# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""The solution I initially thought of. Kinda slow (24 - 28 ms on average) Traverse the tree initially, including all empty nodes. Then invert the tree, and include the nodes again. compare the two sets, if they are the same, the trees are symmetrical. """
from collections import deque
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def traverse(root, nums):
            """
            :type root: TreeNode
            :type nums: List[int]
            :rtype: None
            """
            # pre-order traversal, with a twist: append the empty nodes as well
            # for positioning and comparison of nodes
            if root != None:
                nums.append(root.val)
                traverse(root.left, nums)
                traverse(root.right, nums)
            else:
                nums.append(root)
                
        def invert(root):
            """
            :type root: TreeNode
            :rtype: None """
            if root != None:
                root.left, root.right = root.right, root.left
                invert(root.left)
                invert(root.right)
                
        before = deque()
        reverse = deque()
        
        traverse(root, before)
        invert(root)
        traverse(root, reverse)
        
        if before == reverse:
            return True
        else:
            return False
        

        