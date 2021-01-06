from collections import deque
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:           
        result = []
        
        if root is None: return result
        
        queue = deque()
        queue.append(root)        
        rightToLeft = True
        
        while queue:
            level = deque()
            
            for _ in range(len(queue)):
                node = queue.popleft()
                                        
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
                if rightToLeft:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)
            
            rightToLeft = not rightToLeft
            result.append(list(level))
                           
        return result