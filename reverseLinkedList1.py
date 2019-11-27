# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        curr = head
        prev = None
        while curr != None:
            if prev != None:
                temp = curr.next
                curr.next = head
                prev.next = temp
                head = curr
                curr = prev.next
            else:
                prev = curr
                curr = curr.next
        return head