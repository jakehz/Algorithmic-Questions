# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""10 ms faster than my solution (better than 90%). Credit to Stefan Pochmann"""
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        prev = None
        slow = fast = head
        while fast and fast.next: 
            # move along by twos. when this is at the end, the slow pointer will be at the middle. 
            fast = fast.next.next
            """ we move the previous to the current (slow), point the new previous to the OLD previous value
             and move the slow pointer onto the next node. this results in a reversed linked list until it 
             stops."""
            prev, prev.next, slow = slow, prev, slow.next
        """if at this point the fast pointer does not point to none, that we were able to move 
        along by twos, and counting the initial node this makes the length odd. 
        therefore we can skip the node that slow is at since this is the exact middle. """
        if fast:
            slow = slow.next
        
        # at this point the prev pointer will point to where the end the first half used to be
        # but it is now reversed, so it is the beginning. 
        while prev and prev.val == slow.val:
            slow = slow.next
            prev = prev.next
            
        # if the prev pointer is at none, then it will be a palindrome. otherwise the comparisons did not match
        return not prev
        