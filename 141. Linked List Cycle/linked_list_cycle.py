# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        next = head
        node_map = {}
        
        while next:
            if next in node_map:
                return True
            node_map[next] = True
            next = next.next
        
        return False