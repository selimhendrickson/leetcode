# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        prev = None
        curr = head
        start, end = None, None
        
        if head.next == None: return head
        
        i = 1
        while i != m:
            prev = curr
            curr = curr.next 
            i += 1

        start = prev
        end = curr

        prev = None
        while i < n+1:    
            prev, curr.next, curr = curr, prev, curr.next   
            i += 1
    
        if start: 
            start.next = prev
        else:
            head = prev
        end.next = curr
  
        return head     
   