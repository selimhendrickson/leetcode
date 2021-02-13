from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        ListNode.__lt__ = lambda self, other: self.val < other.val

        resultHead = lastNode = ListNode(0)
        minheap = []

        # add the first node of each list
        for node in lists:
            if node:
                heappush(minheap, (node.val, node))

        while minheap:
            nodeval, node = heappop(minheap)
            lastNode.next = ListNode(nodeval)
            lastNode = lastNode.next      
            if node.next:
                heappush(minheap, (node.next.val, node.next))

        return resultHead.next        