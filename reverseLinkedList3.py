# Definition for singly-linked list.
from typing import List
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def makeList(linked: List[int]) -> ListNode:
    head = None
    prev = None
    curr = None
    for v in linked:
        if prev == None:
            head = ListNode(v)
            prev = head
        else: 
            curr = ListNode(v)
            prev.next = curr
            prev = curr
    return head

def printList(head: ListNode) -> None:
    curr = head
    vals = "["
    while curr != None and curr.next != None:
        vals += str(curr.val) + ","
        curr = curr.next
    vals += str(curr.val) + "]"
    print(vals)

def reverseList(head: ListNode) -> ListNode: 
    curr = head
    prev = None
    while curr != None:
        prev, prev.next,curr = curr, prev, curr.next
    return prev


