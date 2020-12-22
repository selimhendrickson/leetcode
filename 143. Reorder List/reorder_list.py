# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None:
            return head
            
        mid_node = self.find_middle(head)
        mid_node = self.reverse_list(mid_node)

        node = head
        while mid_node.next:
            node.next, mid_node.next, node, mid_node = mid_node, node.next, node.next, mid_node.next
            

    def find_middle(self, head):
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def reverse_list(self, curr):
        prev = None

        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        
        return prev