# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        middle = self.middleNode(head)
        stack = []
        next = head
        
        while next is not middle:
            stack.append(next)
            next = next.next
        
        next = next.next

        while next:
            if stack.pop != next:
                return False
            next = next.next
        
        return True
        
        
    def middleNode(self, head):
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow        