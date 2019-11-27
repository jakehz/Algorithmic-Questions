"""Attempt 1. Uses O(n) time complexity and O(n) memory Identify if the linked list contains a loop. """
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        pointDict = {}
        curr = head
        while curr != None:
            if curr in pointDict:
                return True
            else:
                pointDict[curr] = 1
            curr = curr.next
        return False