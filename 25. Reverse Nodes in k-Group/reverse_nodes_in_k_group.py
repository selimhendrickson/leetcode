# I need to write test cases for this. I first need to extract the building of list nodes into a separate module.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        curr = head
        start = head
        pin = None
        head = None  
        end = start

        while curr:
            i = 1
            while i < k and curr.next:
                curr = curr.next
                i += 1
            pin = curr.next
            curr.next = None
    
            if i == k:
                tmp = self.reverse_all(start)
            else:
                tmp = start
    
            if not head:
                head = tmp
            else:
                end.next = tmp         
                end = start

            curr = pin 
            start = pin

        return head

    def reverse_all(self, head):
        prev = None
        curr = head

        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        return prev        