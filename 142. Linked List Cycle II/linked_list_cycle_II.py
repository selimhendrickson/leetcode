# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        node = head
        node_set = set()
        while node != None:
            if node in node_set:
                return node
            else:
                node_set.add(node)
            node = node.next
        return None