# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        end = head

        if head is None or k == 0:
            return head

        length = 1
        #find the end of the LinkedList
        while end.next is not None:
          end = end.next
          length += 1

        #connect the end to the head
        end.next = head
        
        steps = length - k % length - 1

        #let's find the new head
        end = head
        for i in range(steps):
            end = end.next
            
            
        #set the new head and break the circle
        head = end.next
        end.next = None

        return head

class Solution2:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None or k == 0:
            return head

        end = head  
        length = 1
        #find the end of the LinkedList
        while end.next is not None:
          end = end.next
          length += 1

        #Turn LinkedList into a circle
        end.next = head
        i = 0
        while i < (length - k) % length:
            head = head.next
            i += 1

        end = head
        while length > 1:
            end = end.next
            length -= 1
        
        end.next = None
          
        return head