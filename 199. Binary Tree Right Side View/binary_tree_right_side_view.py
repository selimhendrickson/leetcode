from typing import List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        result = []
        if not root:
            return result
        queue  = deque()
        queue.append(root)
        node = None

        while queue:
            length = len(queue)    
    
            for _ in range(length):
                node = queue.popleft()      
      
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)            
    
            result.append(node.val)

        return result       