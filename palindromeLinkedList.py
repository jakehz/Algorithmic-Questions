# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""Accepted but slow-ish. still technically has O(n) time complexity and O(1) storage"""
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # get the length of the linked list
        curr = head
        length = 0
        while curr != None:
            curr = curr.next
            length += 1
        
        # set the middle point of the linked list
        if length % 2 == 1:
            middle = (length // 2) + 1
        else:
            middle = (length / 2) 
        
        # set the starting point for the second half of the linked list
        start = 0
        midNode = head
        while start != middle:
            midNode = midNode.next
            start += 1
        
        # reverse the second half 
        curr = midNode
        newMid = None
        while curr != None:
            temp = curr.next
            curr.next = newMid
            newMid = curr
            curr = temp
       
        # simultaneously compare the first and second half (reverse)
        curr = head
        while newMid != None:
            if newMid.val != curr.val:
                return False
            newMid = newMid.next
            curr = curr.next
        return True